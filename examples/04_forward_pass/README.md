# Forward Pass (Example #4)

This example shows a **forward pass** through a single dense layer with **two neurons**.

Each neuron computes:
1) a weighted sum: `z = sum(inputs * weights) + bias`  
2) an activation: `a = activation(z)`

We run the same layer twice:
- once with **ReLU**
- once with **Sigmoid**

## How to Run

```bash
python forward_pass.py
```


## What to Observe

* The layer produces two outputs because it has two neurons
* Each neuron has different weights + bias, so they behave differently
* ReLU can output exactly 0 for negative z
* Sigmoid always outputs a value between 0 and 1

## What to Try

1. Change one input value (e.g. set the last input to 30.0)
2. Flip the sign of one weight and see how it changes z
3. Change biases and observe output shifts
4. Add a third neuron (add a new weight list + bias)
5. Add a new activation function (e.g. tanh) and run again

Goal: build intuition for how data flows forward through a layer.
