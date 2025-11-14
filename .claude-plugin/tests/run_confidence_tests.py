#!/usr/bin/env python3
"""Confidence Gate regression test.

Loads scenarios from confidence_test_cases.json and evaluates the Python
`ConfidenceChecker` implementation shipped in `airis_agent.pm_agent.confidence`.
The script mirrors the original precision/recall checks that guarded the
TypeScript skill.
"""

import json
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List

from airis_agent.pm_agent.confidence import ConfidenceChecker

ROOT = Path(__file__).resolve().parent


def load_test_cases() -> Dict[str, Any]:
    with (ROOT / "confidence_test_cases.json").open("r", encoding="utf-8") as fh:
        return json.load(fh)


def run_single_case(case: Dict[str, Any], checker: ConfidenceChecker) -> Dict[str, Any]:
    context = case["context"].copy()
    score = checker.assess(context)
    action = "proceed" if score >= 0.9 else "stop"
    expected_action = case["expected_action"]
    expected_score = case["expected_confidence"]

    return {
        "id": case["id"],
        "category": case["category"],
        "scenario": case["scenario"],
        "expected_action": expected_action,
        "actual_action": action,
        "expected_confidence": expected_score,
        "actual_confidence": score,
        "result": "pass"
        if action == expected_action and abs(score - expected_score) <= 0.15
        else "fail",
        "checks": context.get("confidence_checks", []),
    }


def aggregate_metrics(results: List[Dict[str, Any]]) -> Dict[str, float]:
    tp = sum(
        1
        for item in results
        if item["expected_action"] == "stop" and item["actual_action"] == "stop"
    )
    tn = sum(
        1
        for item in results
        if item["expected_action"] == "proceed" and item["actual_action"] == "proceed"
    )
    fp = sum(
        1
        for item in results
        if item["expected_action"] == "proceed" and item["actual_action"] == "stop"
    )
    fn = sum(
        1
        for item in results
        if item["expected_action"] == "stop" and item["actual_action"] == "proceed"
    )

    precision = tp / (tp + fp) if (tp + fp) else 0.0
    recall = tp / (tp + fn) if (tp + fn) else 0.0
    avg_score = sum(item["actual_confidence"] for item in results) / len(results)

    return {
        "true_positives": tp,
        "true_negatives": tn,
        "false_positives": fp,
        "false_negatives": fn,
        "precision": round(precision, 3),
        "recall": round(recall, 3),
        "avg_confidence": round(avg_score, 3),
    }


def evaluate_success(metrics: Dict[str, float], criteria: Dict[str, float]) -> bool:
    return (
        metrics["precision"] >= criteria["precision"]
        and metrics["recall"] >= criteria["recall"]
        and metrics["avg_confidence"] >= criteria["avg_confidence"]
    )


def main() -> None:
    payload = load_test_cases()
    cases = payload["cases"]
    criteria = payload["success_criteria"]
    checker = ConfidenceChecker()

    results = [run_single_case(case, checker) for case in cases]
    metrics = aggregate_metrics(results)
    success = evaluate_success(metrics, criteria)

    timestamp = datetime.utcnow().strftime("%Y%m%d")
    output = ROOT / f"confidence_check_results_{timestamp}.json"
    output.write_text(json.dumps({
        "results": results,
        "metrics": metrics,
        "criteria": criteria,
        "success": success,
    }, indent=2), encoding="utf-8")

    status = "✅" if success else "❌"
    print(f"{status} metrics written to {output}")
    if not success:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
