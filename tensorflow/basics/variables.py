import tensorflow as tf

# Create a variable
x = tf.Variable([2], dtype=tf.float32)

# Use the variable in an operation
y = tf.constant([3], dtype=tf.float32)
z = tf.multiply(x, y)

# Change the value of the variable
x.assign([4])
z = tf.multiply(x, y)
print(z)
