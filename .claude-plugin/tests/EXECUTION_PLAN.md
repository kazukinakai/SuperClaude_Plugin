# Confidence Check Test Execution Plan

1. Ensure the repository is installed locally ( `uv pip install -e .` ).
2. Run the confidence test harness:
   ```bash
   uv run python plugins/airis-agent/tests/run_confidence_tests.py
   ```
3. Review the generated `confidence_check_results_YYYYMMDD.json` file for metrics.
4. Success criteria (current targets):
   - Precision ≥ 0.90
   - Recall ≥ 0.85
   - Average confidence ≥ 0.85
   - Average token overhead < 150 tokens/test
