import pandas as pd
import numpy as np 
import json

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

ids = cleaned_players["player_id"]

all_matches = []

for i in range(len(ids)):
    player_id = int(ids.iloc[i])  #get the actual player_id from the series

    matches = id_to_matches(player_id)
    matches = matches.sort_values(by="tourney_date")  # sort matches
    if len(matches) > 6:  
        match_data = matches.iloc[1:].values.tolist()
        if int(matches.iloc[0]["winner_id"]) == player_id:
            matches_per_player = [player_id, 1, match_data]
        else:
            matches_per_player = [player_id, 0, match_data]
        all_matches.append(matches_per_player)

import csv
with open("all_matches.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["player_id", "label", "matches"])
    
    for record in all_matches:
        player_id = record[0]
        label = record[1]
        matches = record[2]
        matches_str = json.dumps(matches) 
        writer.writerow([player_id, label, matches_str])

