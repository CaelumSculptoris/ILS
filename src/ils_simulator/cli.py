"""Command-line experiment runner."""

from __future__ import annotations

import argparse
from statistics import mean

from .model import run_experiment


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the offline landscape-sculpting experiment.")
    parser.add_argument("--trials", type=int, default=10)
    parser.add_argument("--seed", type=int, default=0)
    args = parser.parse_args()
    if args.trials < 1:
        parser.error("--trials must be positive")

    results = [run_experiment(args.seed + trial) for trial in range(args.trials)]
    for label in ("ensemble", "lexical"):
        metrics = [getattr(result, label) for result in results]
        print(f"{label:8} precision={mean(m.precision for m in metrics):.3f} "
              f"recall={mean(m.recall for m in metrics):.3f}")


if __name__ == "__main__":
    main()
