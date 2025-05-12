import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf
physical_devices = tf.config.list_physical_devices('GPU')
tf.config.experimental.set_memory_growth(physical_devices[0], True)

# X = tf.constant(4)
# X = tf.constant(4, shape=(1,1), dtype=tf.float32)
# X = tf.constant([[1,2,3],[4,5,6]])
# X = tf.ones((3,3,))
# X = tf.zeros((3,3), dtype=tf.int32)
# X = tf.eye(3)
# X = tf.random.normal((3,3), mean=0, stddev=1)
# X = tf.random.uniform((1,3), minval=0, maxval=1)
# X = tf.range(9)
X = tf.range(start=1, limit=10, delta=2)

print(X)