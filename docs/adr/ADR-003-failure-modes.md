# ADR-003: Failure Modes & Recovery

Date: 2026-10-24
Status: Accepted

## Context
What if agent fails mid-pipeline? Need graceful degradation.

## Decision
- Extractor fails: retry 2 times, else return "No clauses found" with low confidence.
- Comparator fails: return playbook_id as UNKNOWN, log trace_id.
- Risk Scorer fails: default risk = MEDIUM, require human review.
- Memo Writer fails: retry, else return raw comparison table.

All failures logged to traces table with trace_id, agent_name, error.

## Reason
NFR requires graceful degradation, never crash silently. Supports audit and cost < Rs25.

## Consequences
+ System never crashes, auditable
- May need human review for some cases