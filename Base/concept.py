#python 

import tensorflow as tf   #引包
#转换为数字的本来类型
def tranferX(x):
	with tf.Session() as sess:
		x_=sess.run(x)
		return x_
#常量constant
node1=tf.constant(2,tf.float32)#定义节点，值为2
node2=tf.constant(3,tf.float32)#定义节点，值为3
print(node1,node2)

#执行 Session.run()
with tf.Session() as sess:
	node=sess.run([node1,node2])
	print(node)

#占位符placeholder相关
a=tf.placeholder(tf.float32)
b=tf.placeholder(tf.float32)
sum=a+b
print(sum,{a:2,b:3})
with tf.Session() as sess:
	sum_=sess.run(sum,{a:2,b:3})
	print(sum_)
	print("sum",sum)
#lambda表达式
c=lambda x:x+2
print(c(1))

#变量
d=tf.Variable(3)#并没有进行初始化
print(d)#Tensor("Variable/read:0", shape=(), dtype=int32) 输入的float32没有用
with tf.Session() as sess:
	d_=sess.run(d.initialized_value())#如果直接调用 sess.run(d)会报错，所以一定要调用这个函数
	print(d_)#输出3
	#下面是进行全局的所有变量都进行了初始化操作 
	#init = tf.global_variables_initializer()
	#sess.run(init)
	#d_=sess.run(d)#这里就对了
	#print(d_)#输出3
#修改其值
fixD=tf.assign(d,4)#将变量d赋值为4
print("fixD=",fixD)#结果：fixD= Tensor("Assign:0", shape=(), dtype=int32_ref)
fixD_=tranferX(fixD)#将张量改变为数学格式
print("fixD_=",fixD_)#fixD_= 4