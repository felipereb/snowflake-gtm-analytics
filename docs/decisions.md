# Decisions

One entry per decision: what was decided, why, and what was traded off.

## 001. Cost guardrails before anything else

Two extra small warehouses (load and transform) with auto suspend after 60 seconds, and an account level resource monitor that suspends all compute at the credit cap. The trial has a fixed budget, so a runaway query should stop the account instead of spending it.

## 002. Functional roles from day one

LOADER, TRANSFORMER, REPORTER and MCP_READONLY, all rolled up to SYSADMIN. ACCOUNTADMIN is used only for account setup. Each tool connects with the least privileged role it needs.
