# Gradients & Updates (Example #6)

This example shows the core idea of learning:

1) Compute loss  
2) Compute the gradient (direction of change)  
3) Update the parameter to reduce the loss  

We use **MSE loss** for one value:

- Loss: `L = (y_true - y_pred)^2`
- Gradient: `dL/dy_pred = 2 * (y_pred - y_true)`

Then we do one gradient descent step:

`y_pred_new = y_pred - learning_rate * gradient`

## How to Run

```bash
python mse_gradient.py
```

## What to Observe

* The gradient points in the direction that increases the loss
* Subtracting the gradient moves y_pred toward y_true
* The loss should decrease after the update

## What to Try

1. Change learning_rate:
Try 0.01 (small step)
Try 1.0 (may overshoot)

2. Change initial y_pred:
Set y_pred = 10.0
Watch how the gradient direction flips

3. Run the update multiple times:
Copy the update into a loop and see y_pred converge toward y_true

Goal: build intuition that gradients drive learning.