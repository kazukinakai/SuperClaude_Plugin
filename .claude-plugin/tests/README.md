# Airis Agent Plugin Tests

This directory stores stress tests for the confidence-check skill and plugin execution plans. The suite mirrors the original Airis Agent verification flow.

- `confidence_test_cases.json` enumerates pass/fail confidence scenarios with expected scores and actions.
- `run_confidence_tests.py` executes the TypeScript/py compiled skill (via local shim) and computes precision/recall.
- `EXECUTION_PLAN.md` documents how to run the tests in CI or manually.
