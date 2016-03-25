#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
   Title: Sentence Crusher
   Authors: Jonas, Glenn, Emil, JanCato
   Started: 16.03.2016

"""
# --- Global modules ---
import time
import random

# --- Local modules ---
from data import DataGuy, GameGuy, DBGuy, LogicGuy
from graphics import GfxGuy

def game():
    # ------------ INITialize objects ------------- # 
    D = DataGuy()
    DB = DBGuy()
    Gfx = GfxGuy()
    Game = GameGuy()
    Logic = LogicGuy()

    # -------------- Start new_game ------------- #
    Gfx.print_opening()
    Game.user_input_name(D)

    while True:
        # -------------------- INIT/input -------------------- #
        Gfx.greet_user(D)
        Game.user_input_level(D)           

        # -------------------- GRAPHICS -------------------- #
        Gfx.print_highscore(D, DB)             
        
        input("\n\tNow, press enter and get ready to write!")
        
        Gfx.countdown_321()
        D.store_clock_before()
        
        # -------------------- CORE GAME -------------------- #
        Gfx.show_string(D)  
        Game.input_user_string(D)
        
        # --------------------- LOGIC ----------------------- #
        D.store_clock_after()
        D.store_datetime()
        Logic.calc_points(D, Gfx)

        # ---------------- DATABASE DUMP -------  -----------#
        DB.store_data(D)
        print(D.highscore_dict)
        # ---------------- DATA TO SERVER -------  -----------#
        listing = DB.post_data(D)
        print('Listing is:\n', listing)

        # -------------------- INPUT -------------------- #
        start_again = Game.continue_game()

        if start_again is True:
            D.__init__()
            continue
        else:
            break


if __name__ == "__main__":
    game()


