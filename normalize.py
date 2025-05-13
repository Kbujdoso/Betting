import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.environ['TF_USE_LEGACY_KERAS'] = '1'

import tensorflow as tf
import tensorflow_decision_forests as tfdf
import numpy as np
import pandas as pd
import tf_keras
import keras
import math 
import re
from datetime import datetime
import ast


def surface(x):
    if x == "Hard":
        return 1
    elif x == "Clay":
        return 2
    elif x == "Grass": 
        return 3
    elif x == "Carpet": 
        return 4

def seed(x):
    if pd.isna(x):
        return 0
    try:
        return int(x)
    except ValueError:
        return 0
   
def entry(x): 
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
    elif pd.isna(x):
        return 6

def hand(x):
    if x == "R": 
        return 0
    elif x == "L":
        return 1
    else: 
        return 2

def height(x):
    if pd.isna(x):
        return 185
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
 
def score(x):
    result = ""
    reg_sets = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    inside_parentheses = False
    for i in range(len(x)):
        if x[i] == "(":
            inside_parentheses = True
        elif x[i] == ")":
            inside_parentheses = False
        elif not inside_parentheses:
            result += x[i]
    result = re.split(r'[-\s]', result)
    for i in range(len(result)):
        if result[i] != "RET":
            reg_sets[i] = result[i]
        else: 
            return reg_sets
    return reg_sets

    
def date_to_unix(x):
    try: 
        date = datetime.strptime(str(x), "%Y%m%d")
        return int(date.timestamp())
    except ValueError: 
        return -1

def rank(x):
    if pd.isna(x):
        return -1
    else: 
        return int(x)
def to_number(x):
    if pd.isna(x):
        return -1
    else: 
        return int(x)

#need a function for main.py which can handle new databases this code was for this database
"""
players = pd.read_csv("players.csv")
matches = pd.read_csv("clean_matches_5.csv", low_memory=False)


def cleaning_matches(x):
    pass #remove where ace_w = None (This prevents that those matches which are too old to have good data being selected.)

def clean_and_numerical_database_setter(players, matches):
    clean_matches = cleaning_matches(matches)
    clean_players = players[
        (players["player_id"].isin(clean_matches["winner_id"])) | 
        (players["player_id"].isin(clean_matches["loser_id"]))
                            ]


    name_id = clean_players[["player_id", "name_first", "name_last"]]

    name_id.loc[:,"name_last"] = name_id["name_last"].apply(lambda x: x.split(" ")[-1])
    name_id.loc[:,"name_first"] = name_id["name_first"].apply(lambda x: x.split(" ")[0])
    name_id.to_csv("name_and_ids.csv", index=False)

    clean_matches = clean_matches[["surface", "draw_size", "tourney_date", "match_num", "winner_id", "winner_seed", "winner_entry", "winner_hand", "winner_ht", "winner_age", "loser_id", "loser_seed", "loser_entry", "loser_hand", "loser_ht", "loser_age", "score", "best_of", "round", "minutes", "w_ace", "w_df", "w_svpt", "w_1stIn", "w_1stWon", "w_2ndWon", "w_SvGms", "w_bpSaved", "w_bpFaced", "l_ace", "l_df", "l_svpt", "l_1stIn", "l_1stWon", "l_2ndWon", "l_SvGms", "l_bpSaved", "l_bpFaced", "winner_rank", "winner_rank_points", "loser_rank", "loser_rank_points"]]
    clean_matches = pd.read_csv("num_matches2.csv")

    clean_matches["surface"] = clean_matches["surface"].apply(surface)
    clean_matches["tourney_date"] = clean_matches["tourney_date"].apply(date_to_unix)


    clean_matches["winner_seed"] = clean_matches["winner_seed"].apply(seed)
    clean_matches["loser_seed"] = clean_matches["loser_seed"].apply(seed)

    clean_matches["winner_entry"] = clean_matches["winner_entry"].apply(entry)
    clean_matches["loser_entry"] = clean_matches["loser_entry"].apply(entry)

    clean_matches["winner_hand"] = clean_matches["winner_hand"].apply(hand)
    clean_matches["loser_hand"] = clean_matches["loser_hand"].apply(hand)

    clean_matches["winner_ht"] = clean_matches["winner_ht"].apply(height)
    clean_matches["loser_ht"] = clean_matches["loser_ht"].apply(height)

    clean_matches["winner_rank"] = clean_matches["winner_rank"].apply(rank)
    clean_matches["loser_rank"] = clean_matches["loser_rank"].apply(rank)

    clean_matches["winner_rank_points"] = clean_matches["winner_rank_points"].apply(rank)
    clean_matches["loser_rank_points"] = clean_matches["loser_rank_points"].apply(rank)

    clean_matches["round"] = clean_matches["round"].apply(round)

    clean_matches["score"] = clean_matches["score"].apply(score)
    clean_matches.to_csv("num_matches2.csv", index=False)
"""
columns = [
        "surface", "draw_size", "tourney_date", "match_num", "winner_id", "winner_seed",
        "winner_entry", "winner_hand", "winner_ht", "winner_age", "loser_id", "loser_seed",
        "loser_entry", "loser_hand", "loser_ht", "loser_age", "best_of", "round",
        "minutes", "w_ace", "w_df", "w_svpt", "w_1stIn", "w_1stWon", "w_2ndWon", "w_SvGms",
        "w_bpSaved", "w_bpFaced", "l_ace", "l_df", "l_svpt", "l_1stIn", "l_1stWon", "l_2ndWon",
        "l_SvGms", "l_bpSaved", "l_bpFaced", "winner_rank", "winner_rank_points", "loser_rank",
        "loser_rank_points"
    ] 




data_set = pd.read_csv("num_matches2.csv", low_memory=False)

data_set['score'] = data_set['score'].apply(ast.literal_eval)
set_oszlopok = data_set['score'].apply(pd.Series)
set_oszlopok.columns = [f'set_{i+1}' for i in range(set_oszlopok.shape[1])]
data_set = data_set.drop(columns=['score']) 
data_set = pd.concat([data_set, set_oszlopok], axis=1)
sets = [
    "set_1","set_2","set_3","set_4","set_5","set_6","set_7","set_8","set_9","set_10"
    ]
data_set[sets] = data_set[sets].applymap(lambda x: int(x) if str(x).isdigit() else -1)

columns = [
        "surface", "draw_size", "tourney_date", "match_num", "winner_id", "winner_seed",
        "winner_entry", "winner_hand", "winner_ht", "winner_age", "loser_id", "loser_seed",
        "loser_entry", "loser_hand", "loser_ht", "loser_age", "best_of", "round",
        "minutes", "w_ace", "w_df", "w_svpt", "w_1stIn", "w_1stWon", "w_2ndWon", "w_SvGms",
        "w_bpSaved", "w_bpFaced", "l_ace", "l_df", "l_svpt", "l_1stIn", "l_1stWon", "l_2ndWon",
        "l_SvGms", "l_bpSaved", "l_bpFaced", "winner_rank", "winner_rank_points", "loser_rank",
        "loser_rank_points","set_1","set_2","set_3","set_4","set_5","set_6","set_7","set_8","set_9","set_10"
    ]
        

data_set[columns] = data_set[columns].applymap(float)
data_set.to_csv("all_float_matches2.csv", index = False)