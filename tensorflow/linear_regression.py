import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# Actual parameters
a = 3
b = 2
n_samples = 100

# Generate X values
X = np.random.rand(n_samples, 1)

# Generate corresponding Y values
Y = a * X + b + np.random.randn(n_samples, 1) * 0.1

W = tf.Variable(np.random.randn(), name="weight")
b = tf.Variable(np.random.randn(), name="bias")

laearning_rate = 0.1
num_epochs = 1000  # The number of iterations

optimizer = tf.optimizers.SGD(learning_rate=laearning_rate)

# Linear regression function
def linear_regression(x):
    return W * x + b

# Cost function
def mean_square(y_pred, y_true):
    return tf.reduce_mean(tf.square(y_pred - y_true))


for epoch in range(num_epochs):
    # Using GradientTape for automatic differentiation.
    with tf.GradientTape() as g:
        pred = linear_regression(X)
        loss = mean_square(pred, Y)

    # Compute gradients
    gradients = g.gradient(loss, [W, b])

    # Update W and b
    optimizer.apply_gradients(zip(gradients, [W, b]))

    # Print the loss every 50 iterations
    if (epoch+1) % 50 == 0:
        print("Epoch: %i, Loss: %f" % (epoch+1, loss))


plt.scatter(X, Y, color='blue', label='Original data')
plt.plot(X, np.array(W * X + b), color='red', label='Fitted line')
plt.legend()
plt.show()