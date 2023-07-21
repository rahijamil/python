import tensorflow as tf

# Define a constant tensor
x = tf.constant([2], dtype=tf.float32)
print(x)

# Define another constant tensor
y = tf.constant([3], dtype=tf.float32)

# Perform and operation
z = tf.multiply(x, y)
print(z)