# Activation Functions (Example #3)

This folder contains two classic activation functions:

- **Sigmoid**: squashes values into the range (0, 1)
- **ReLU**: outputs 0 for negative inputs and keeps positive inputs unchanged

Activation functions introduce **non-linearity**, which is essential for neural networks to learn complex patterns.

## How to Run

```bash
python sigmoid.py
python relu.py
```

## What to Observe

### Sigmoid

* Large negative inputs produce values close to 0
* Large positive inputs produce values close to 1
* Around 0, sigmoid changes most quickly

#### ReLU

* Negative inputs become 0
* Positive inputs pass through unchanged
* ReLU is simple and widely used in hidden layers

## What to Try

* Add more test values (e.g., -10, 10)
* Compare how sigmoid and ReLU treat negative inputs
* Change the test ranges and see how outputs behave

Goal: build intuition for how activations shape signals flowing through a network.