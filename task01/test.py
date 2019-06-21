import tensorflow as tf
import tensorflow.keras as kr
hello = tf.constant('Hello, world!')

sess = tf.Session()
print(sess.run(hello))
sess.close()