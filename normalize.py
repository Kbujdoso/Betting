import os
# Keep using Keras 2
os.environ['TF_USE_LEGACY_KERAS'] = '1'

import tensorflow_decision_forests as tfdf

import numpy as np
import pandas as pd
import tensorflow as tf
import tf_keras
import math 
import keras
from datetime import datetime


def normalize_all(x): 
    norm = keras.layers.Normalization()
    norm.adapt(x)
    return norm(x)


def surface(x):
    if x == "Hard":
        return 1
    elif x == "Clay":
        return 2
    elif x == "Grass": 
        return 3
    elif x == "Carpet": 
        return 4

def year(x): 
    x = x[:4]
    return int(x)

def num_seed(x):
    if x is None: 
        return 0
    else: 
        return int(x)
   
def num_entry(x): 
    if x == "LL": 
        return 1
    elif x == "Q":
        return 2
    elif x == "WC":
        return 3
    elif x == "PR":
        return 4
    elif x == "SE":
        return 5
    elif x == None:
        return 6

def hand(x):
    if x == "R": 
        return 0
    elif x == "L":
        return 1
    else: 
        return 2

def height(x):
    if x is None: 
        return int(185)
    else:
        return int(x)

def round(x):
    round_encoding = {
    'R128': 0,
    'R64': 1,
    'R32': 2,
    'R16': 3,
    'QF': 4,
    'SF': 5,
    'F': 6,
    'BR': 7,
    'RR': 8
}
    return round_encoding.get(x)

def already_num(x):
    return int(x)
    
def score():
    pass 

def date_to_unix(x):
      date = datetime.strptime(x, "%Y%m%d")
      return int(date.timestamp())

print(date_to_unix("20250415"))

players = pd.read_csv("players.csv")

clean_matches = pd.read_csv("clean_matches_5.csv", low_memory=False)

clean_players = players[
    (players["player_id"].isin(clean_matches["winner_id"])) | 
    (players["player_id"].isin(clean_matches["loser_id"]))
                        ]


clean_players.to_csv("clean_players.csv", index=False)



cleaned_players = pd.read_csv("clean_players.csv")


name_id = cleaned_players[["player_id", "name_first", "name_last"]]

name_id["name_last"] = name_id["name_last"].apply(lambda x: x.split(" ")[-1])
name_id["name_first"] = name_id["name_first"].apply(lambda x: x.split(" ")[0])
name_id.to_csv("name_and_ids.csv", index=False)