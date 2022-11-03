

import tensorflow as tf
print(tf.__version__)
mnist = tf.keras.datasets.fashion_mnist
print(mnist)

(training_images, training_labels), (test_images, test_labels) = mnist.load_data()
import matplotlib.pyplot as plt
plt.imshow(training_images[0])
print(training_labels[0])
print(training_images[0])