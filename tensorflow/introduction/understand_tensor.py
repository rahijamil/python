import tensorflow as tf

# 0-D tensor (scaler)
scaler = tf.constant(7)

# 1-D tensor (vector)
vector = tf.constant([10, 7])


# 2-D tensor (matrix)
matrix = tf.constant([[10, 7], [7, 10]])

# 3-D tensor
tensor = tf.constant([[[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]])
