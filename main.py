#!/usr/bin/env python3
"""
Kleines Coin‑Flip‑Simulations‑Skript 🪙
Verwendet NumPy, um eine bestimmte Anzahl von Münzwürfen zu simulieren.
"""

import argparse
import numpy as np


def simulate_flips(n: int) -> tuple[int, int]:
    """Simuliert n Würfe und gibt (heads, tails) zurück."""
    flips = np.random.randint(0, 2, size=n)  # 0 = tails, 1 = heads
    heads = int(flips.sum())
    tails = n - heads
    return heads, tails


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Simuliere eine Anzahl von Münzwürfen mithilfe von NumPy."
    )
    parser.add_argument(
        "-n", "--num", type=int, default=100, help="Anzahl der Würfe (Standard: 100)"
    )
    args = parser.parse_args()

    heads, tails = simulate_flips(args.num)
    print(f"🪙 Ergebnisse für {args.num} Würfe: Heads = {heads}, Tails = {tails}")


if __name__ == "__main__":
    main()