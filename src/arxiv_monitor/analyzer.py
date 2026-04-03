from __future__ import annotations

import json
import os
import re

from .models import AnalysisResult, Paper

try:
    from openai import OpenAI
except ImportError:  # pragma: no cover - optional dependency at runtime
    OpenAI = None


WORLD_MODEL_TERMS = {
    "world model",
    "world models",
    "world action model",
    "world action models",
}

ROBOT_TERMS = {
    "robot",
    "robotic",
    "robotics",
    "manipulation",
    "grasping",
    "navigation",
    "embodied",
    "locomotion",
    "uav",
    "drone",
    "autonomous driving",
    "autonomous vehicle",
    "self-driving",
}

FOUNDATION_TERMS = {
    "foundation model",
    "foundation models",
    "vision-language-action",
    "vision language action",
    "vla",
    "generalist robot",
    "generalist robotics",
    "embodied foundation model",
    "robot foundation model",
    "robotic foundation model",
    "large language model",
    "multimodal",
    "action model",
}

MODEL_BASED_TERMS = {
    "latent dynamics",
    "dynamics model",
    "dynamics models",
    "predictive control",
    "model predictive control",
    "model-based reinforcement learning",
    "model-based rl",
}

NON_TARGET_TERMS = {
    "power grid",
    "grid stability",
    "transmission system",
    "turbofan",
    "wavefront",
    "exoplanet",
    "astronomy",
    "medical imaging",
    "education",
    "speech",
    "finance",
    "weather",
    "protein",
    "earth observation",
    "remote sensing",
    "electricity",
    "video game",
    "video games",
    "gaming",
}


class PaperAnalyzer:
    def __init__(self, config: dict) -> None:
        self.config = config
        self.openai_model = config["analysis"]["openai_model"]
        self.min_score = config["analysis"]["min_heuristic_score"]
        self.api_key = os.getenv("OPENAI_API_KEY", "")
        self.client = OpenAI(api_key=self.api_key) if self.api_key and OpenAI else None

    def analyze(self, paper: Paper) -> AnalysisResult:
        if self.client is not None:
            try:
                return self._analyze_with_openai(paper)
            except Exception:
                pass
        return self._analyze_with_heuristics(paper)

    def _analyze_with_openai(self, paper: Paper) -> AnalysisResult:
        prompt = f"""
You are screening newly published arXiv papers.

Return strict JSON with keys:
- is_relevant: boolean
- topic: short English label
- reason: short Chinese explanation
- summary_zh: one-sentence Chinese summary
- confidence: integer 0-100

Relevant means the paper is materially related to one of these:
1. world models for embodied agents or robots
2. robot foundation models
3. vision-language-action models
4. embodied generalist models for robotics
5. model-based robot learning/planning with learned dynamics

Not relevant if it only mentions generic LLMs, VLMs, dynamics, or planning without a meaningful robotics / embodied / world-model connection.

Paper title: {paper.title}
Paper abstract: {paper.abstract}
Categories: {", ".join(paper.categories)}
""".strip()

        response = self.client.responses.create(
            model=self.openai_model,
            input=prompt,
        )
        content = getattr(response, "output_text", "").strip()
        data = json.loads(content)
        return AnalysisResult(
            is_relevant=bool(data["is_relevant"]),
            topic=str(data["topic"]).strip(),
            reason=str(data["reason"]).strip(),
            summary_zh=str(data["summary_zh"]).strip(),
            confidence=max(0, min(100, int(data["confidence"]))),
            method="openai",
            score=int(data["confidence"]),
        )

    def _analyze_with_heuristics(self, paper: Paper) -> AnalysisResult:
        text = self._normalize_text(f"{paper.title} {paper.abstract}")
        score = 0
        matched: list[str] = []

        world_hits = self._find_terms(text, WORLD_MODEL_TERMS)
        robot_hits = self._find_terms(text, ROBOT_TERMS)
        foundation_hits = self._find_terms(text, FOUNDATION_TERMS)
        model_based_hits = self._find_terms(text, MODEL_BASED_TERMS)
        non_target_hits = self._find_terms(text, NON_TARGET_TERMS)

        score += len(world_hits) * 4
        score += len(robot_hits) * 2
        score += len(foundation_hits) * 3
        score += len(model_based_hits) * 2
        score -= len(non_target_hits) * 3

        matched.extend(world_hits)
        matched.extend(robot_hits)
        matched.extend(foundation_hits)
        matched.extend(model_based_hits)

        has_world_model_connection = bool(world_hits) and (
            bool(robot_hits)
            or "policy" in text
            or "planning" in text
            or "agent" in text
            or "autonomous driving" in text
        )
        has_robot_foundation_connection = bool(foundation_hits) and (
            bool(robot_hits)
            or "vision language action" in text
            or "vision-language-action" in paper.abstract.lower()
        )
        has_model_based_robot_connection = bool(model_based_hits) and bool(robot_hits)

        is_relevant = score >= self.min_score and (
            has_world_model_connection
            or has_robot_foundation_connection
            or has_model_based_robot_connection
        )

        if non_target_hits and not robot_hits and not has_robot_foundation_connection:
            is_relevant = False

        topic = "robot_foundation" if has_robot_foundation_connection else "world_model"
        reason = "命中关键词: " + ", ".join(sorted(set(matched))[:6]) if matched else "未命中高价值关键词"
        summary = self._build_summary(paper, topic)
        confidence = max(20, min(95, score * 10))
        return AnalysisResult(
            is_relevant=is_relevant,
            topic=topic,
            reason=reason,
            summary_zh=summary,
            confidence=confidence,
            method="heuristic",
            score=score,
        )

    @staticmethod
    def _build_summary(paper: Paper, topic: str) -> str:
        abstract = paper.abstract.strip()
        if not abstract:
            return "摘要为空，无法生成总结。"
        first_sentence = abstract.split(". ")[0].strip().rstrip(".")
        prefix = "世界模型方向" if topic == "world_model" else "机器人大模型方向"
        return f"{prefix}: {first_sentence[:180]}。"

    @staticmethod
    def _normalize_text(text: str) -> str:
        normalized = text.lower().replace("-", " ").replace("/", " ")
        return re.sub(r"\s+", " ", normalized)

    @staticmethod
    def _find_terms(text: str, terms: set[str]) -> list[str]:
        matches: list[str] = []
        for term in terms:
            pattern = r"\b" + re.escape(term).replace(r"\ ", r"\s+") + r"\b"
            if re.search(pattern, text):
                matches.append(term)
        return matches
