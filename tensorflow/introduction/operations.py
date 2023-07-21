import tensorflow as tf

# Define two 2-d tensors (matrices)
x = tf.constant([[1, 2], [3, 4]])
y = tf.constant([[5, 6], [7, 8]])

# Add
add_result = tf.add(x, y)
print("Addition: \n", add_result.numpy())

# Subtract
sub_result = tf.subtract(x, y)
print("Subtraction: \n", sub_result.numpy())

# Multiply
mul_result = tf.multiply(x, y)
print("Multiplication: \n", mul_result.numpy())

# Divide
div_result = tf.divide(x, y)
print("Division: \n", div_result.numpy())

# Matrix multiply
matmul_result = tf.matmul(x, y)
print("Matrix multiplication: \n", matmul_result.numpy())
