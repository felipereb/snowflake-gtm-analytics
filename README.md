# Snowflake GTM Analytics

A small go-to-market analytics platform on Snowflake, built as a personal learning project.

Everything here is synthetic. No real company data, names, metrics or code are used.

## What it does

1. Generates synthetic B2B SaaS CRM data with Python (accounts, contacts, opportunities, opportunity stage history, activities, subscriptions).
2. Loads it into Snowflake through an internal stage with `COPY INTO`.
3. Models it with dbt (staging, intermediate, marts) into a star schema for the sales funnel.
4. Exposes funnel and pipeline metrics through a Snowflake semantic view, queried in natural language with Cortex Analyst and the Snowflake managed MCP server.
5. Documents one measured optimization with runtime and credits before and after.

## Status

Work in progress. Week 1 of 4: account setup and data loading.

## Repository layout

```
infra/       Snowflake setup scripts (roles, warehouses, database, stages)
generator/   Python generator for the synthetic CRM data
dbt/         dbt project (from week 2)
docs/        Architecture diagram, decisions, benchmark results
scripts/     Repo checks used in CI
```

## Cost guardrails

Extra small warehouses, auto suspend after 60 seconds, and an account level resource monitor that suspends all compute at the credit cap.
