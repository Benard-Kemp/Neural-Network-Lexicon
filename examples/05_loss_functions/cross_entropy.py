# cross_entropy.py
# Example #5 — Cross-Entropy loss for classification

import math


def cross_entropy(y_true_index, predicted_probs, eps=1e-12):
    """
    Cross-Entropy for a single sample in multi-class classification.

    - y_true_index: the correct class index (e.g., 0, 1, 2)
    - predicted_probs: list of probabilities (must sum ~ 1.0)

    loss = -log(p_true)
    """
    if not (0 <= y_true_index < len(predicted_probs)):
        raise ValueError("y_true_index is out of range")

    p_true = predicted_probs[y_true_index]

    # Avoid log(0) which is undefined
    p_true = max(p_true, eps)

    return -math.log(p_true)


if __name__ == "__main__":
    # Example: 3-class classification
    # Model outputs probabilities for each class:
    predicted_probs = [0.10, 0.70, 0.20]

    # Suppose the true class is index 1 (the second class)
    y_true_index = 1

    loss = cross_entropy(y_true_index, predicted_probs)

    print("Cross-Entropy Loss (Classification)")
    print("-" * 35)
    print("predicted_probs:", predicted_probs)
    print("true_class_index:", y_true_index)
    print("loss            :", loss)
