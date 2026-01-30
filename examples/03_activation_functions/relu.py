# relu.py
# Example #3 — ReLU activation (Rectified Linear Unit)

def relu(x):
    """ReLU(x) = max(0, x)"""
    return x if x > 0 else 0.0


if __name__ == "__main__":
    # Try a mix of negative, zero, and positive values
    test_values = [-3.0, -1.0, -0.1, 0.0, 0.2, 1.0, 5.0]

    print("ReLU Activation")
    print("-" * 30)
    for x in test_values:
        print(f"x={x:>5} -> relu(x)={relu(x):>5}")
