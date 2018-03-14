from __future__ import print_function
import tensorflow as tf

# matrix 1*2
matrix1 = tf.constant([[3, 3]])
# matrix 2*1
matrix2 = tf.constant([[2],
                       [2]])
product = tf.matmul(matrix1,matrix2)

# method 1
# sess = tf.Session()
# result = sess.run(product)
# print(result)
# sess.close()

# method 2
with tf.Session() as sess:
    result2 = sess.run(product)
    print(result2)