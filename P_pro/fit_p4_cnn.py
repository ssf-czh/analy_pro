import tensorflow.compat.v1 as tf

tf.disable_v2_behavior()
import numpy as np
import matplotlib.pyplot as plt

plt.ion()
plt.show()


def add_layer(inputs, in_size, out_size, activation_function=None):
    Weights = tf.Variable(tf.random_normal([in_size, out_size]))
    biases = tf.Variable(tf.zeros([1, out_size]) + 0.1)
    # 神经网络预测值
    Wx_plus_b = tf.matmul(inputs, Weights) + biases
    # 激励函数
    if activation_function is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_function(Wx_plus_b)
    return outputs


# 构建数据
x_data = np.linspace(-1, 1, 300, dtype=np.float32)[:, np.newaxis]
noise = np.random.normal(0, 0.05, x_data.shape).astype(np.float32)
y_data = np.square(x_data) - 0.5 + noise

# 定义输入
xs = tf.placeholder(tf.float32, [None, 1])
ys = tf.placeholder(tf.float32, [None, 1])

# 定义隐藏层
l1 = add_layer(xs, 1, 20, activation_function=tf.nn.relu)

# 定义输出层
prediction = add_layer(l1, 20, 1, activation_function=None)

# 损失函数：误差平方和求均值
loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - prediction), reduction_indices=[1]))

# 优化器最小化损失函数
train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

# 初始化变量
init = tf.global_variables_initializer()

# 开启会话
sess = tf.Session()
sess.run(init)

# 显示图片框
fig = plt.figure()

# 连续画图ax,数据点
ax = fig.add_subplot(1, 1, 1)
ax.scatter(x_data, y_data)

# 训练
for i in range(5000):

    sess.run(train_step, feed_dict={xs: x_data, ys: y_data})
    if i % 50 == 0:
        # print(sess.run(loss, feed_dict={xs: x_data, ys: y_data}))
        # 除了第一次,抹除之前预测线
        try:
            ax.lines.remove(lines[0])
        except Exception:
            pass
        prediction_value = sess.run(prediction, feed_dict={xs: x_data})
        # 把预测用一条线表示
        lines = ax.plot(x_data, prediction_value, 'r-', lw=5)
        plt.pause(0.1)
        print(sess.run(loss, feed_dict={xs: x_data, ys: y_data}))
        print(i)