import pandas as pd 
import numpy as np

import scraper as sc

def player_finder_tester(x, y, z):
        if x: 
            print(f"{y}.test passed ({z} function's test)")
        else: 
            print(f"{y}. test failed ({z} function's test)")






player_finder_tester(sc.player_finder("Ion Tiriac") == 100035, 1, "player_finder")
player_finder_tester(sc.player_finder("Jose Pereira") == 105700, 2, "player_finder")
player_finder_tester(sc.player_finder("David Susanto") == 105812, 3, "player_finder")
player_finder_tester(sc.player_finder("Mousheg Hovhannisyan") == 105855, 4, "player_finder")
player_finder_tester(sc.player_finder("Sekou Bangoura") == 105871, 5, "player_finder")


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
data_set[columns] = data_set[columns].applymap(float)

for i in range(len(columns)):
    if data_set[columns[i]].apply(lambda x : isinstance(x,float)).all() :
         print(f"{columns[i]} passed")
    else:
        print(f"{columns[i]} failed")

