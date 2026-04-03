from __future__ import annotations

import smtplib
from email.message import EmailMessage

from .models import Paper


def send_email(config: dict, papers: list[Paper]) -> None:
    username = __import__("os").getenv("SMTP_USERNAME", "")
    password = __import__("os").getenv("SMTP_PASSWORD", "")
    if not username or not password:
        raise RuntimeError("SMTP_USERNAME or SMTP_PASSWORD is missing.")

    email_cfg = config["email"]
    message = EmailMessage()
    message["Subject"] = f"[arXiv Monitor] {len(papers)} new relevant papers"
    message["From"] = f'{email_cfg["sender_name"]} <{username}>'
    message["To"] = email_cfg["recipient"]

    if papers:
        text_lines = [
            "以下是本次筛选出的 arXiv 新论文:",
            "",
        ]
        html_lines = [
            "<html><body>",
            "<p>以下是本次筛选出的 arXiv 新论文:</p>",
            "<ul>",
        ]

        for paper in papers:
            text_lines.append(f"- {paper.title}")
            text_lines.append(f"  {paper.abs_url}")
            html_lines.append(f'<li><a href="{paper.abs_url}">{paper.title}</a></li>')

        html_lines.extend(["</ul>", "</body></html>"])
    else:
        text_lines = [
            "今天没有筛选到新的相关论文。",
        ]
        html_lines = [
            "<html><body><p>今天没有筛选到新的相关论文。</p></body></html>",
        ]

    message.set_content("\n".join(text_lines))
    message.add_alternative("\n".join(html_lines), subtype="html")

    if email_cfg["use_ssl"]:
        with smtplib.SMTP_SSL(email_cfg["smtp_host"], email_cfg["smtp_port"], timeout=30) as server:
            server.login(username, password)
            server.send_message(message)
    else:
        with smtplib.SMTP(email_cfg["smtp_host"], email_cfg["smtp_port"], timeout=30) as server:
            server.starttls()
            server.login(username, password)
            server.send_message(message)
