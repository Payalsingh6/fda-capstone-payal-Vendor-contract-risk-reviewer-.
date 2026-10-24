# ADR-002: Tool-calling vs Pure Prompting

Date: 2026-10-24
Status: Accepted

## Context
Agents need to call external tools (DB, vector store, risk calculator).

## Options
1. Tool-calling (function calling)
2. Pure prompting (LLM outputs JSON)

## Decision
Tool-calling.

## Reason
- Reliability: forces structured output with clause_number, playbook_id - no hallucination.
- Security: tools sandboxed, input validation, no prompt injection.
- Observability: each tool call logged with trace_id.

## Consequences
+ Accurate citations, safe
- Need tool schemas maintained