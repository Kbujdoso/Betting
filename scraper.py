import pandas as pd
import numpy as np 
import json

cleaned_players = pd.read_csv("name_and_ids.csv")
clean_matches = pd.read_csv("all_float_matches2.csv")


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

def match_searcher(id,date, match_num): 
    matches = id_to_matches(id)
    matches = matches.sort_values(by=["tourney_date", "match_num"])  # sort matches
    for i in range(len(matches)):
        if matches.iloc[i]["tourney_date"] == date and matches.iloc[i]["match_num"] == match_num:
            x = i
            break
    if len(matches) >= x+15:  
        match_data = matches.iloc[x:x+15].values.tolist()
        return match_data

ids = cleaned_players["player_id"]


def data_set(ids):
    all_matches = []
    training_data_lists = []
    for i in range(len(ids)):
        player_id = int(ids.iloc[i])  #get the actual player_id from the series

        matches = id_to_matches(player_id)
        matches = matches.sort_values(by=["tourney_date", "match_num"])  # sort matches
        date = int(matches.iloc[0]["tourney_date"])  
        match_num = int(matches.iloc[0]["match_num"])

        
        result = -1
        if int(matches.iloc[0]["winner_id"]) == player_id:
            result = 1
        else:
            result = 0
        m1 = match_searcher(matches.iloc[0]["winner_id"],date,match_num)
        m2 = match_searcher(matches.iloc[0]["loser_id"],date,match_num)
        matches_clean = []
        if m1 != None and m2 != None:
            for i in range(len(m1)):
                for j in range(len(m1[i])):
                    matches_clean.append(m1[i][j])
            for i in range(len(m2)):
                for j in range(len(m2[i])):
                    matches_clean.append(m2[i][j])
                training_data_lists.append((matches_clean, result))


import json
def visual_check(x):

    with open("visual_test.json", "w", encoding="utf-8") as f:
        json.dump(x, f)



