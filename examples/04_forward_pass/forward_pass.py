# forward_pass.py
# Example #4 — Forward pass through a single dense layer (2 neurons)

import math


def weighted_sum(inputs, weights, bias):
    """output = sum(inputs[i] * weights[i]) + bias"""
    if len(inputs) != len(weights):
        raise ValueError("inputs and weights must have the same length")

    total = 0.0
    for x, w in zip(inputs, weights):
        total += x * w
    return total + bias


def relu(x):
    """ReLU(x) = max(0, x)"""
    return x if x > 0 else 0.0


def sigmoid(x):
    """Sigmoid(x) = 1 / (1 + exp(-x))"""
    return 1.0 / (1.0 + math.exp(-x))


def forward_layer(inputs, layer_weights, layer_biases, activation_fn):
    """
    Compute outputs for a dense layer.

    - layer_weights: list of weight lists (one list per neuron)
    - layer_biases: list of bias values (one per neuron)
    - activation_fn: relu or sigmoid (or another function)
    """
    if len(layer_weights) != len(layer_biases):
        raise ValueError("layer_weights and layer_biases must match in length")

    outputs = []
    for neuron_weights, neuron_bias in zip(layer_weights, layer_biases):
        z = weighted_sum(inputs, neuron_weights, neuron_bias)  # pre-activation
        a = activation_fn(z)                                  # activation
        outputs.append(a)
    return outputs


if __name__ == "__main__":
    # Inputs (features)
    inputs = [1.0, 2.0, 3.0]

    # A dense layer with 2 neurons:
    # Each neuron has its own weights (one per input) and its own bias.
    layer_weights = [
        [0.5, -1.0, 0.2],   # neuron 1 weights
        [-0.2, 0.9, 0.1],   # neuron 2 weights
    ]
    layer_biases = [0.1, -0.3]

    print("Inputs:", inputs)

    # Forward pass with ReLU
    relu_outputs = forward_layer(inputs, layer_weights, layer_biases, relu)
    print("\nForward pass (ReLU):", relu_outputs)

    # Forward pass with Sigmoid
    sigmoid_outputs = forward_layer(inputs, layer_weights, layer_biases, sigmoid)
    print("Forward pass (Sigmoid):", sigmoid_outputs)
