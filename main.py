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

cleaned_players = pd.read_csv("name_and_ids.csv")
clean_matches = pd.read_csv("all_float_matches2.csv")
ids = cleaned_players["player_id"]

training_data = scraper.data_set(ids)

