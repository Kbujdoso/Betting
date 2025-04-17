import pandas as pd 
import numpy as np

import scraper as sc

def tester(x, y, z):
        if x: 
            print(f"{y}.test passed ({z} function's test)")
        else: 
            print(f"{y}. test failed ({z} function's test)")






tester(sc.player_finder("Ion Tiriac") == 100035, 1, "player_finder")
tester(sc.player_finder("Jose Pereira") == 105700, 2, "player_finder")
tester(sc.player_finder("David Susanto") == 105812, 3, "player_finder")
tester(sc.player_finder("Mousheg Hovhannisyan") == 105855, 4, "player_finder")
tester(sc.player_finder("Sekou Bangoura") == 105871, 5, "player_finder")



