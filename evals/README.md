# Day 03 - Golden Evaluation Dataset

## Purpose
Golden dataset for evaluating contract deviation detection.

## Files
- `golden.jsonl` - 5 curated contracts with expected deviations and risk
- `eval_config.json` - Evaluation configuration and thresholds

## Metrics
- Accuracy: exact match of deviations
- Precision/Recall: per-deviation detection
- Risk Alignment: LOW/MEDIUM/HIGH/CRITICAL classification match

## Risk Levels
- LOW: compliant contract
- MEDIUM: minor commercial deviations
- HIGH: missing FDA / low liability
- CRITICAL: one-sided indemnity / unlimited liability
