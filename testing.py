import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

model = tf.keras.models.Sequential([
  tf.keras.layers.InputLayer(input_shape=(12,1)),
#  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.LSTM(12),
  tf.keras.layers.Dense(2)
])
