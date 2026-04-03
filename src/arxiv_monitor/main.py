from __future__ import annotations

import argparse

from .analyzer import PaperAnalyzer
from .arxiv_client import ArxivClient
from .archive_writer import append_title_archive
from .config import load_config
from .emailer import send_email
from .readme_writer import update_readme
from .reporter import build_report, save_report


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Monitor arXiv for world-model and robot-foundation papers.")
    parser.add_argument("--config", default="config.yaml", help="Path to config YAML.")
    parser.add_argument("--dry-run", action="store_true", help="Run analysis but skip sending email.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    config = load_config(args.config)

    report_file = config["output"]["report_file"]
    title_archive_file = config["output"]["title_archive_file"]

    client = ArxivClient(
        base_url=config["arxiv"]["base_url"],
        user_agent=config["arxiv"]["user_agent"],
    )
    analyzer = PaperAnalyzer(config)

    recent_papers = client.fetch_recent_papers(config)
    relevant_pairs = []

    for paper in recent_papers:
        analysis = analyzer.analyze(paper)
        if analysis.is_relevant:
            relevant_pairs.append((paper, analysis))

    report = build_report(relevant_pairs)
    save_report(report_file, report)
    append_title_archive(title_archive_file, relevant_pairs, config["arxiv"]["lookback_days"])
    update_readme("README.md", relevant_pairs, config["arxiv"]["lookback_days"])

    if config["email"]["enabled"] and not args.dry_run:
        send_email(config, [paper for paper, _ in relevant_pairs])

    print(f"Fetched recent papers: {len(recent_papers)}")
    print(f"Relevant papers found: {len(relevant_pairs)}")
    print(f"Report written to: {report_file}")
    print(f"Title archive written to: {title_archive_file}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
