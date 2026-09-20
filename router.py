"""Small, explainable IT support ticket router."""

from dataclasses import dataclass
import re
from typing import Iterable

CATEGORIES = {
    "security": {
        "phishing", "malware", "ransomware", "breach", "suspicious",
        "password", "mfa", "login", "unauthorized", "virus", "credential",
    },
    "network": {
        "wifi", "network", "vpn", "dns", "router", "latency",
        "internet", "connection", "offline",
    },
    "software": {
        "install", "update", "crash", "application", "software",
        "license", "error", "bug",
    },
    "hardware": {
        "laptop", "monitor", "keyboard", "mouse", "battery",
        "printer", "screen", "dock",
    },
}


@dataclass(frozen=True)
class RouteResult:
    category: str
    confidence: float
    matched_terms: tuple[str, ...]


def _tokens(text: str) -> set[str]:
    return set(re.findall(r"[a-z0-9']+", text.lower()))


def route_ticket(text: str) -> RouteResult:
    """Route a ticket using transparent keyword scoring."""
    tokens = _tokens(text)
    scores: dict[str, list[str]] = {}

    for category, terms in CATEGORIES.items():
        scores[category] = sorted(tokens & terms)

    category = max(scores, key=lambda name: len(scores[name]))
    matches = scores[category]
    total_matches = sum(len(items) for items in scores.values())

    if not matches:
        return RouteResult("general", 0.0, ())

    confidence = len(matches) / total_matches if total_matches else 0.0
    return RouteResult(category, round(confidence, 2), tuple(matches))


def route_many(tickets: Iterable[str]) -> list[RouteResult]:
    return [route_ticket(ticket) for ticket in tickets]


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Route an IT support ticket.")
    parser.add_argument("ticket", help="Ticket text")
    args = parser.parse_args()

    result = route_ticket(args.ticket)
    print(f"category={result.category}")
    print(f"confidence={result.confidence:.2f}")
    print("matched_terms=" + ",".join(result.matched_terms))
