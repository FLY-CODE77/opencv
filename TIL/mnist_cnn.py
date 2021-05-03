import tensorflow as tf     
from tensorflow.examples.tutorials.mnist import input_data
from tensorflow.python.framework import graph_util
from tensorflow.python.platform import gfile

tf.logging.set_verbosity(tf.logging.ERROR)

mnist = input_data.read_data_sets("./MNIST_data/", one_hot=True)
learning_rate = 0.001
training_epochs = 20
batch_size = 100

# MODEL CONFiGURATI
X = tf.placeholder(tf.float32, [None, 28, 28, 1], name='data')
Y = tf.placeholder(tf.float32, [None, 10])
# tf.placeholder
# shape [None, 28, 28, 1] None 은 크기가 정해지지 않음, input 크기에 따라 유동적으로 할당 


conv1 = tf.layers.conv2d(X, 10, [3, 3], padding='same', activation=tf.nn.relu)
# tf.layers.conv2d(X,10, [3,3], padding ='same', activation=tf.nn.relu)
# X 이미지 입력으로 받아서 3,3 커널이 가로 세로 3칸씩 이동하면서 출력으로 10개의 체널을 relu activation을 걸치게 된다.

pool1 = tf.layers.max_pooling2d(conv1, [2, 2], strides=2, padding='same')
# conv1의 이미지를 받아서 [2,2] 사이지의 풀링 커널이 사로 세로 2칸씩 이동하면서 
# padding=same 특정맵의 크기를 동일하게 하기 위해 주위에 0으로 패딩하는 방법
# 패딩 없이 순수한 입력 배열만 활용하여 맵을 만드는 경우를 vaild padding 
# 패딩을 함으로서 모서리의 중요한 정보를 놓치지 않기 위해서 보통을 SAME 패딩을 많이 사용한다 

conv2 = tf.layers.conv2d(pool1, 20, [3, 3], padding='same', activation=tf.nn.relu)
pool2 = tf.layers.max_pooling2d(conv2, [2, 2], strides=2, padding='same')

fc1 = tf.contrib.layers.flatten(pool2)
fc2 = tf.layers.dense(fc1, 200, activation=tf.nn.relu)

logits = tf.layers.dense(fc2, 10, activation=None)
output = tf.nn.softmax(logits, name='prob')

cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(labels=Y, logits=logits))
optimizer = tf.train.AdamOptimizer(learning_rate).minimize(cost)

#
# Training
#
sess = tf.Session()
sess.run(tf.global_variables_initializer())
total_batch = int(mnist.train.num_examples / batch_size)

print('Start learning!')
for epoch in range(training_epochs):
    total_cost = 0

    for i in range(total_batch):
        batch_xs, batch_ys = mnist.train.next_batch(batch_size)
        batch_xs = batch_xs.reshape(-1, 28, 28, 1)
        _, cost_val = sess.run([optimizer, cost], feed_dict={X: batch_xs, Y: batch_ys})
        total_cost += cost_val

    print('Epoch: {0}, Avg. Cost = {1:.4f}'.format(epoch + 1, total_cost/total_batch))

print('Learning finished!')

# Test the results
is_correct = tf.equal(tf.argmax(logits, 1), tf.argmax(Y, 1))
acc = tf.reduce_mean(tf.cast(is_correct, tf.float32))
accuracy = sess.run(acc, feed_dict={
                    X: mnist.test.images.reshape(-1, 28, 28, 1), Y: mnist.test.labels})
print('Test Accuracy:', accuracy)

# Freeze variables and save pb file
output_graph_def = graph_util.convert_variables_to_constants(sess, sess.graph_def, ['prob'])
with gfile.FastGFile('./mnist_cnn.pb', 'wb') as f:
    f.write(output_graph_def.SerializeToString())

print('mnist_cnn.pb file is created successfully!!')