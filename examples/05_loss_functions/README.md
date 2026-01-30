# Loss Functions (Example #5)

Loss functions measure **how wrong** a prediction is.

This folder contains two classic losses:

- **MSE (Mean Squared Error)** — common in regression
- **Cross-Entropy** — standard for classification

## How to Run

```bash
python mse.py
python cross_entropy.py
```

## What to Observe

### MSE (Regression)

* The loss is the squared difference between prediction and truth
* Larger errors grow quickly because of squaring

### Cross-Entropy (Classification)

* The loss depends mainly on the probability assigned to the true class
* If the model assigns low probability to the true class, loss is large
* If the model assigns high probability to the true class, loss is small

## What to Try

### For mse.py

* Change y_pred closer to y_true and see loss shrink
* Change y_pred far away and see loss grow

### For cross_entropy.py

* Change predicted_probs so the true class has:
0.90 probability (loss becomes small)
0.01 probability (loss becomes very large)
* Try changing the true class index

Goal: build intuition that training is about reducing loss over time.