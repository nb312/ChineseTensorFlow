#python
import tensorflow as tf
node1=tf.constant(2,tf.float32)#定义节点，值为2
node2=tf.constant(3,tf.float32)#定义节点，值为3
sess=tf.Session()
node=tf.add(node1,node2)
sess.run(node)
writer = tf.summary.FileWriter("test_1", node.graph)
