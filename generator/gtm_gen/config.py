"""Generator settings. Boilerplate: volumes per scale and the random seed.

The business parameters (stages, conversion rates, deal sizes, cycle times)
belong in entities.py, where you define them.
"""

from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class Scale:
    name: str
    n_accounts: int
    contacts_per_account: int
    opportunities_per_account: float
    activities_per_opportunity: int


SCALES: dict[str, Scale] = {
    # Fast iteration while developing.
    "dev": Scale("dev", n_accounts=500, contacts_per_account=4,
                 opportunities_per_account=2.0, activities_per_opportunity=15),
    # Default for the project.
    "small": Scale("small", n_accounts=10_000, contacts_per_account=5,
                   opportunities_per_account=2.5, activities_per_opportunity=25),
    # Week 4 benchmark: large enough that pruning and clustering show up in the numbers.
    "large": Scale("large", n_accounts=200_000, contacts_per_account=6,
                   opportunities_per_account=3.0, activities_per_opportunity=60),
}


@dataclass(frozen=True)
class Settings:
    scale: Scale
    seed: int = 42
    start_date: date = date(2023, 1, 1)
    end_date: date = date(2026, 10, 31)
