import pandas as pd
import numpy as np 

cleaned_players = pd.read_csv("name_and_ids.csv")
clean_matches = pd.read_csv("num_matches2.csv")


def player_finder(x): 
    playername = x.split(" ")
    match = cleaned_players[(cleaned_players["name_first"] == playername[0]) &
            (cleaned_players["name_last"] == playername[1])]
    return int(match.iloc[0]["player_id"])

def id_to_matches(x): 
    matches = clean_matches[
        (clean_matches["winner_id"] == x) | 
        (clean_matches["loser_id"] == x)
        ]
    return matches 

def all_id(x): 
    ids = []
    ids = cleaned_players["player_id"]