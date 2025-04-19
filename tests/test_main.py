"""
Pytest‑Suite für main.py
Stellt sicher, dass simulate_flips erwartungsgemäß funktioniert.
"""

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import math
from main import simulate_flips


def test_total_counts():
    """Heads + Tails == n."""
    n = 1000
    heads, tails = simulate_flips(n)
    assert heads + tails == n


def test_probability_close_to_half():
    """
    Für große n sollte der Anteil von Heads ~50 % sein.
    Wir erlauben eine 5‑σ‑Abweichung basierend auf Binomialverteilung.
    """
    n = 10_000
    heads, tails = simulate_flips(n)
    p_hat = heads / n
    sigma = math.sqrt(0.25 / n)  # sqrt(p*(1-p)/n) mit p=0.5
    # 5‑sigma‑Intervall
    assert abs(p_hat - 0.5) <= 5 * sigma
