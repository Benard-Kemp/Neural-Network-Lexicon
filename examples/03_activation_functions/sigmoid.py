# sigmoid.py
# Example #3 — Sigmoid activation

import math


def sigmoid(x):
    """Sigmoid(x) = 1 / (1 + exp(-x))"""
    return 1.0 / (1.0 + math.exp(-x))


if __name__ == "__main__":
    # Values chosen to show the S-shape behavior clearly
    test_values = [-6.0, -3.0, -1.0, 0.0, 1.0, 3.0, 6.0]

    print("Sigmoid Activation")
    print("-" * 30)
    for x in test_values:
        print(f"x={x:>5} -> sigmoid(x)={sigmoid(x):.6f}")
