"""Entity generation. YOU WRITE THIS FILE (week 1 learning step).

Each function receives a numpy Generator (`rng`), a Faker instance and the
Settings, plus any parent rows it depends on, and returns a list of dicts.
The writer turns them into files; the CLI wires everything together.

Decide and write down, before coding:
- Funnel stages, their order, and which ones count as closed won / closed lost.
- Conversion rate from each stage to the next, and how it varies by segment.
- Deal size (ACV) distribution by segment, and the sales cycle length.
- How stage history is produced (every opportunity walks the stages in order,
  can it skip or go backwards?).
- Which activity types exist and how their volume relates to deal progress.
- How subscriptions follow closed won opportunities (start date, term, renewals).

Make it deterministic: only use `rng` and `fake` (seeded in the CLI),
never `random` or the current time.

Column lists below are a starting proposal. Change them as you see fit.
"""

from typing import Any

import numpy as np
from faker import Faker

from .config import Settings

Row = dict[str, Any]


def make_accounts(rng: np.random.Generator, fake: Faker, s: Settings) -> list[Row]:
    """account_id, account_name, industry, segment, country, employee_count, created_at"""
    raise NotImplementedError


def make_contacts(rng: np.random.Generator, fake: Faker, s: Settings,
                  accounts: list[Row]) -> list[Row]:
    """contact_id, account_id, first_name, last_name, title, email, created_at"""
    raise NotImplementedError


def make_opportunities(rng: np.random.Generator, fake: Faker, s: Settings,
                       accounts: list[Row]) -> list[Row]:
    """opportunity_id, account_id, owner_id, opportunity_type, lead_source,
    amount, currency, stage_name, is_closed, is_won, created_at, close_date"""
    raise NotImplementedError


def make_stage_history(rng: np.random.Generator, s: Settings,
                       opportunities: list[Row]) -> list[Row]:
    """stage_history_id, opportunity_id, stage_name, amount, entered_at"""
    raise NotImplementedError


def make_activities(rng: np.random.Generator, fake: Faker, s: Settings,
                    opportunities: list[Row], contacts: list[Row]) -> list[Row]:
    """Written as JSON Lines and loaded into a VARIANT column on purpose.

    Suggested shape: activity_id, activity_type, occurred_at, opportunity_id,
    contact_id, owner_id, plus a nested `details` object whose keys depend on
    the type (call duration, email subject, meeting attendees list).
    """
    raise NotImplementedError


def make_subscriptions(rng: np.random.Generator, s: Settings,
                       opportunities: list[Row]) -> list[Row]:
    """subscription_id, account_id, opportunity_id, product, mrr, currency,
    start_date, end_date, status"""
    raise NotImplementedError
