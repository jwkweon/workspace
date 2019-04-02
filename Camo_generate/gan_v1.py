import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import os
import cv2

mnist = input_data.read_data_sets("./mnist/data/", one_hot=True)
X = tf.placeholder(tf.float32, [None, 56 * 56]) # MNIST = 28*28
Z = tf.placeholder(tf.float32, [None, 100]) # Noise Dimension = 128

# ********* G-Network (Hidden Node # = 256)
G_W1 = tf.Variable(tf.random_normal([100, 512], stddev=0.01))
G_W2 = tf.Variable(tf.random_normal([512, 56 * 56], stddev=0.01))
G_b1 = tf.Variable(tf.zeros([512]))
G_b2 = tf.Variable(tf.zeros([56 * 56]))

def generator(noise_z): # 128 -> 256 -> 28*28
    hidden = tf.nn.relu(tf.matmul(noise_z, G_W1) + G_b1)
    output = tf.nn.sigmoid(tf.matmul(hidden, G_W2) + G_b2)
    return output

# ********* D-Network (Hidden Node # = 256)
D_W1 = tf.Variable(tf.random_normal([56 * 56, 512], stddev=0.01))
D_W2 = tf.Variable(tf.random_normal([512, 1], stddev=0.01))
D_b1 = tf.Variable(tf.zeros([512]))
D_b2 = tf.Variable(tf.zeros([1]))

def discriminator(inputs): # 28*28 -> 256 -> 1
    hidden = tf.nn.relu(tf.matmul(inputs, D_W1) + D_b1)
    output = tf.nn.sigmoid(tf.matmul(hidden, D_W2) + D_b2)
    return output

# ********* Generation, Loss, Optimization and Session Init.
G = generator(Z)
loss_D = -tf.reduce_mean(tf.log(discriminator(X)) + tf.log(1 - discriminator(G)))
loss_G = -tf.reduce_mean(tf.log(discriminator(G)))
train_D = tf.train.AdamOptimizer(learning_rate=0.0002).minimize(loss_D, var_list=[D_W1, D_b1, D_W2, D_b2])
train_G = tf.train.AdamOptimizer(learning_rate=0.0002).minimize(loss_G, var_list=[G_W1, G_b1, G_W2, G_b2])

sess = tf.Session()
sess.run(tf.global_variables_initializer())

if not os.path.exists('out/'):
    os.makedirs('out/')

# ********* Training and Testing
noise_test = np.random.normal(size=(10, 100)) # 10 = Test Sample Size, 128 = Noise Dimension
for epoch in range(200): # 200 = Num. of Epoch

    for i in range(100): # 100 = Batch Size
        batch_xs, _ = mnist.train.next_batch(100)
        batch_xs_2 = batch_xs[28*28/100,:]
        batch_xs_2 = np.reshape(batch_xs_2,[28,28])
        batch_xs_56 = cv2.resize(batch_xs_2, (56, 56), interpolation=cv2.INTER_LINEAR)
        batch_xs_56 = np.reshape(batch_xs_56,[-1, 56*56])

        noise = np.random.normal(size=(100, 100))

        sess.run(train_D, feed_dict={X: batch_xs_56, Z: noise})
        sess.run(train_G, feed_dict={Z: noise})

    if epoch == 0 or (epoch + 1) % 10 == 0: # 10 = Saving Period
        samples = sess.run(G, feed_dict={Z: noise_test})

        fig, ax = plt.subplots(1, 10, figsize=(10, 1))
        for i in range(10):
            ax[i].set_axis_off()
            ax[i].imshow(np.reshape(samples[i], (56, 56)))
        plt.savefig('out/{}.png'.format(str(epoch).zfill(3)), bbox_inches='tight')
        plt.close(fig)
