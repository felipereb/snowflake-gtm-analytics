"""Command line entry point. Boilerplate.

Usage:
    gtm-gen --scale dev --out ../data/raw
"""

import argparse
from pathlib import Path

import numpy as np
from faker import Faker

from . import entities
from .config import SCALES, Settings
from .writer import write_csv_gz, write_jsonl_gz


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate synthetic CRM data.")
    parser.add_argument("--scale", choices=SCALES.keys(), default="dev")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--out", type=Path, default=Path("data/raw"))
    args = parser.parse_args()

    settings = Settings(scale=SCALES[args.scale], seed=args.seed)
    rng = np.random.default_rng(settings.seed)
    fake = Faker()
    Faker.seed(settings.seed)

    accounts = entities.make_accounts(rng, fake, settings)
    contacts = entities.make_contacts(rng, fake, settings, accounts)
    opportunities = entities.make_opportunities(rng, fake, settings, accounts)
    stage_history = entities.make_stage_history(rng, settings, opportunities)
    activities = entities.make_activities(rng, fake, settings, opportunities, contacts)
    subscriptions = entities.make_subscriptions(rng, settings, opportunities)

    out: Path = args.out
    counts = {
        "accounts": write_csv_gz(accounts, out / "accounts" / "accounts.csv.gz"),
        "contacts": write_csv_gz(contacts, out / "contacts" / "contacts.csv.gz"),
        "opportunities": write_csv_gz(opportunities,
                                      out / "opportunities" / "opportunities.csv.gz"),
        "opportunity_stage_history": write_csv_gz(
            stage_history, out / "opportunity_stage_history" / "opportunity_stage_history.csv.gz"),
        "activities": write_jsonl_gz(activities, out / "activities" / "activities.jsonl.gz"),
        "subscriptions": write_csv_gz(subscriptions,
                                      out / "subscriptions" / "subscriptions.csv.gz"),
    }
    for name, n in counts.items():
        print(f"{name:<28}{n:>12,}")


if __name__ == "__main__":
    main()
