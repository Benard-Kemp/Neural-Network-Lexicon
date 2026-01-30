# Weights & Bias — Weighted Sum (Example #2)

This example demonstrates the core computation inside a neuron:

**output = sum(inputs[i] * weights[i]) + bias**

Weights determine how strongly each input influences the output.  
Bias shifts the output up or down.

## How to Run

```bash
python weighted_sum.py
```

## What to Try

1. Change one input value (e.g., set the last input to 30.0)
2. Flip the sign of a weight in Neuron A (e.g., change -1.0 to 1.0)
3. Set bias_a = 0.0 and observe the shift
4. Add a 4th input and a 4th weight to both neurons

Goal: build intuition for how weights and bias shape the output.