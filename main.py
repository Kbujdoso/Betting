import os
# Keep using Keras 2
os.environ['TF_USE_LEGACY_KERAS'] = '1'

import tensorflow_decision_forests as tfdf

import numpy as np
import pandas as pd
import tensorflow as tf
import tf_keras
import math
import ast 
import scraper
import matplotlib.pyplot as plt 
from sklearn.model_selection import train_test_split



cleaned_players = pd.read_csv("name_and_ids.csv")
clean_matches = pd.read_csv("all_float_matches2.csv")
ids = cleaned_players["player_id"]

training_data = scraper.data_set(ids)
x, y = zip(*training_data)
x_train, x_test, y_train, y_test = train_test_split(list(x), list(y), test_size=0.2)


train_dataset = tf.data.Dataset.from_tensor_slices((x_train, y_train)).shuffle(100).batch(32)
test_dataset = tf.data.Dataset.from_tensor_slices((x_test, y_test)).batch(32)


model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(1530,)),
  tf.keras.layers.Dense(512, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(256, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dense(1, activation='sigmoid')
])


model.compile(
    optimizer=tf.keras.optimizers.Adam(0.001),
    loss=tf.keras.losses.BinaryCrossentropy(),
    metrics=[tf.keras.metrics.BinaryAccuracy()]
    )

model.fit(
    train_dataset,
    epochs = 6,
    validation_data = test_dataset,
)



"""for i, (features, label) in enumerate(training_data):
    arr = np.array(features)
    if np.isnan(arr).any() or np.isinf(arr).any():
        print(f"Hiba a(z) {i}. mintánál: van benne NaN vagy inf")"""