# mse.py
# Example #5 — Mean Squared Error (MSE) loss for regression

def mse(y_true, y_pred):
    """
    Mean Squared Error for a single value:
    MSE = (y_true - y_pred)^2
    """
    return (y_true - y_pred) ** 2


if __name__ == "__main__":
    # Imagine a regression prediction (e.g., house price, temperature)
    y_true = 3.0
    y_pred = 2.2

    loss = mse(y_true, y_pred)

    print("MSE Loss (Regression)")
    print("-" * 30)
    print("y_true:", y_true)
    print("y_pred:", y_pred)
    print("loss  :", loss)
