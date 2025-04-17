import pandas as pd
import numpy as np 

cleaned_players = pd.read_csv("name_and_ids.csv")

def player_finder(x): 
    playername = x.split(" ")
    match = cleaned_players[(cleaned_players["name_first"] == playername[0]) &
            (cleaned_players["name_last"] == playername[1])]
    return int(match.iloc[0]["player_id"])



print(player_finder("Ion Tiriac"))