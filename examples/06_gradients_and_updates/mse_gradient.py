# mse_gradient.py
# Example #6 — Gradient of MSE and a single gradient descent update

def mse(y_true, y_pred):
    """MSE for a single value: (y_true - y_pred)^2"""
    return (y_true - y_pred) ** 2


def mse_gradient(y_true, y_pred):
    """
    d/d(y_pred) of (y_true - y_pred)^2

    If L = (y_true - y_pred)^2
    then dL/dy_pred = 2 * (y_pred - y_true)
    """
    return 2.0 * (y_pred - y_true)


if __name__ == "__main__":
    # Target and initial prediction (think: model output)
    y_true = 3.0
    y_pred = 0.0

    learning_rate = 0.1

    # Before update
    loss_before = mse(y_true, y_pred)
    grad = mse_gradient(y_true, y_pred)

    # Gradient descent update:
    # y_pred_new = y_pred - lr * gradient
    y_pred_new = y_pred - learning_rate * grad

    # After update
    loss_after = mse(y_true, y_pred_new)

    print("MSE Gradient + One Update Step")
    print("-" * 35)
    print("y_true        :", y_true)
    print("y_pred (before):", y_pred)
    print("loss (before) :", loss_before)
    print("gradient      :", grad)
    print("learning_rate :", learning_rate)
    print("y_pred (after):", y_pred_new)
    print("loss (after)  :", loss_after)
