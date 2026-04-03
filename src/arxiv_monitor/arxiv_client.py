from __future__ import annotations

from datetime import datetime, timedelta, timezone
import time

import feedparser
import requests

from .models import Paper


TIME_FORMAT = "%Y-%m-%dT%H:%M:%SZ"


class ArxivClient:
    def __init__(self, base_url: str, user_agent: str) -> None:
        self.base_url = base_url
        self.user_agent = user_agent

    def fetch_recent_papers(self, config: dict) -> list[Paper]:
        lookback_days = config["arxiv"]["lookback_days"]
        cutoff = datetime.now(timezone.utc) - timedelta(days=lookback_days)
        deduped: dict[str, Paper] = {}
        queries = config["arxiv"]["queries"]

        for index, query_cfg in enumerate(queries):
            papers = self._fetch_query(query_cfg["search_query"], query_cfg["max_results"])
            for paper in papers:
                if paper.published_at < cutoff:
                    continue
                existing = deduped.get(paper.paper_id)
                if existing is None:
                    paper.matched_queries.append(query_cfg["name"])
                    deduped[paper.paper_id] = paper
                else:
                    if query_cfg["name"] not in existing.matched_queries:
                        existing.matched_queries.append(query_cfg["name"])

            if index < len(queries) - 1:
                time.sleep(5)

        return sorted(deduped.values(), key=lambda item: item.published_at, reverse=True)

    def _fetch_query(self, search_query: str, max_results: int) -> list[Paper]:
        response = requests.get(
            self.base_url,
            params={
                "search_query": search_query,
                "start": 0,
                "max_results": max_results,
                "sortBy": "submittedDate",
                "sortOrder": "descending",
            },
            headers={"User-Agent": self.user_agent},
            timeout=30,
        )
        response.raise_for_status()
        feed = feedparser.parse(response.text)
        papers: list[Paper] = []

        for entry in feed.entries:
            paper_id = self._normalize_paper_id(entry.id)
            abs_url = f"https://arxiv.org/abs/{paper_id}"
            pdf_url = f"https://arxiv.org/pdf/{paper_id}.pdf"
            authors = [author.name.strip() for author in getattr(entry, "authors", [])]
            categories = [tag.term for tag in getattr(entry, "tags", [])]
            papers.append(
                Paper(
                    paper_id=paper_id,
                    title=" ".join(entry.title.split()),
                    abstract=" ".join(entry.summary.split()),
                    abs_url=abs_url,
                    pdf_url=pdf_url,
                    published_at=datetime.strptime(entry.published, TIME_FORMAT).replace(tzinfo=timezone.utc),
                    updated_at=datetime.strptime(entry.updated, TIME_FORMAT).replace(tzinfo=timezone.utc),
                    authors=authors,
                    categories=categories,
                    matched_queries=[],
                )
            )
        return papers

    @staticmethod
    def _normalize_paper_id(raw_id: str) -> str:
        paper_id = raw_id.rstrip("/").split("/")[-1]
        if "v" in paper_id:
            return paper_id.split("v")[0]
        return paper_id
