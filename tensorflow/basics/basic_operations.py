import tensorflow as tf

# Addition
x = tf.constant([2], dtype=tf.float32)
y = tf.constant([2], dtype=tf.float32)
z = tf.add(x, y)
print(z)

# Reshape
x = tf.constant([[2, 3], [4, 5]], dtype=tf.float32)
y = tf.reshape(x, [1, 4])
print(y)
