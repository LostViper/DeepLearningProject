import tensorflow as tf
import cv2 as cv

constant = tf.constant("hello world")
sess = tf.Session()

print(sess.run(constant))

print(cv.__version__)
