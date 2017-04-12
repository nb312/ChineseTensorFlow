[相关源代码concept.py](https://github.com/nb312/ChineseTensorFlow/blob/master/Base/concept.py)
# 张量Tensor
 0维张量=标量  
 1维张量=数组  
 2维张量=坐标  
 3维张量=3维空间坐标  
 ...  
 n维张量=n维空间坐标  

---

# 常量 constant
   
    import tensorflow as tf   #引包
    node1=tf.constant(2,tf.float32)#定义节点，值为2
    node2=tf.constant(3,tf.float32)#定义节点，值为3
	print(node1,node2)

结果： Tensor("Const:0", shape=(), dtype=float32) Tensor("Const_1:0", shape=(), dtype=float32)
说明这里node1是一个标量

---
# 输出一般的值Session.run()
    with tf.Session() as sess:
    	sess.run([node1,node2])
结果：[2.0, 3.0]

----
# 占位符 placeholder
---
#### 使用
```
    a=tf.placeholder(tf.float32) #未知维度
	b=tf.placeholder(tf.float32)
	sum=a+b
	print(sum,{a:2,b:3})#这里并没有赋值给sum 只是确定了sum的类型以及a,b的值及类型
```
结果：Tensor("add:0", dtype=float32) {<tf.Tensor 'Placeholder:0' shape=<unknown> dtype=float32>: 2, <tf.Tensor 'Placeholder_1:0' shape=<unknown> dtype=float32>: 3}
输出的还是张量 但是两个的维度未知，输出的为标量  
```
        with tf.Session() as sess:
    		sum_=sess.run(sum,{a:2,b:3})#如果输入sess.run(sum)将会报错误，所以只有执行了前面的才会返回想要的值，但sum依然是张量形式的标量
    		print(sum_)
		print(sum)
```
结果：5.0  
     Tensor("add:0", dtype=float32)
     
#### 和lambda表达式的比较
```
    c=lambda x:x+2
    print(c(1))#输出3
	#他们都是输入一个值 然后进行计算
```
# 变量 Variables
```
    d=tf.Variable(3)#并没有进行初始化，只是类型的确认
    print(d) #结果：Tensor("Variable/read:0", shape=(), dtype=int32) 输入的float32没有用
    with tf.Session() as sess:
    	d_=sess.run(d.initialized_value())#如果直接调用 sess.run(d)会报错，所以一定要调用这个函数
		print(d_)##输出3
		#下面是进行全局的所有变量都进行了初始化操作 
		#init = tf.global_variables_initializer()
		#sess.run(init)
		#d_=sess.run(d)#这里就对了
		#print(d_)#输出3
```
# 修改变量值
```
    fixD=tf.assign(d,4)#将变量d赋值为4
    print("fixD=",fixD)#结果：fixD= Tensor("Assign:0", shape=(), dtype=int32_ref)
    fixD_=tranferX(fixD)#将张量改变为数学格式
    print("fixD_=",fixD_)#fixD_= 4
```

