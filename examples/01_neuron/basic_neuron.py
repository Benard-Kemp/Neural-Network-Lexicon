# basic_neuron.py
# A minimal example of what a single neuron computes

# Input values (features)
inputs = [1.0, 2.0, 3.0]

# Weights applied to each input
weights = [0.5, -1.0, 0.2]

# Bias term (shifts the output)
bias = 0.1

# Compute the weighted sum
weighted_sum = 0.0
for x, w in zip(inputs, weights):
    weighted_sum += x * w

# Add the bias
output = weighted_sum + bias

# Display the result
print("Neuron output:", output)
