# weighted_sum.py
# Example #2 — Weights & Bias (the weighted sum a neuron computes)

def weighted_sum(inputs, weights, bias):
    """
    Compute the core neuron calculation:
    output = sum(inputs[i] * weights[i]) + bias
    """
    if len(inputs) != len(weights):
        raise ValueError("inputs and weights must have the same length")

    total = 0.0
    for x, w in zip(inputs, weights):
        total += x * w

    return total + bias


if __name__ == "__main__":
    # Same inputs, two different parameter settings
    inputs = [1.0, 2.0, 3.0]

    # Neuron A parameters
    weights_a = [0.5, -1.0, 0.2]
    bias_a = 0.1

    # Neuron B parameters (different weights + bias => different behavior)
    weights_b = [-0.2, 0.9, 0.1]
    bias_b = -0.3

    out_a = weighted_sum(inputs, weights_a, bias_a)
    out_b = weighted_sum(inputs, weights_b, bias_b)

    print("Inputs:", inputs)
    print("\nNeuron A")
    print("  Weights:", weights_a)
    print("  Bias:", bias_a)
    print("  Output:", out_a)

    print("\nNeuron B")
    print("  Weights:", weights_b)
    print("  Bias:", bias_b)
    print("  Output:", out_b)
