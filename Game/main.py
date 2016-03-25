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
import logics
import database

from guys import DataGuy, GameGuy, GfxGuy


def game():
    # ------------ INITialize objects ------------- # 
    D = DataGuy()
    Gfx = GfxGuy()
    Game = GameGuy()

    # -------------- Start new_game ------------- #
    Gfx.print_opening()
    Game.user_input_name(D)

    while True:
        # -------------------- INIT/input -------------------- #
        Gfx.greet_user(D)
        Game.user_input_level(D)           

        # -------------------- GRAPHICS -------------------- #
        Gfx.print_highscore(D)             
        
        input("\n\tNow, press enter and get ready to write!")
        
        Gfx.countdown_321()
        D.store_clock_before()
        
        # -------------------- CORE GAME -------------------- #
        Gfx.show_string(D)  
        Game.input_user_string(D)
        
        # --------------------- LOGIC ----------------------- #
        D.store_clock_after()
        D.store_datetime()
        logics.calc_points(D, Gfx)

        # ---------------- DATABASE DUMP -------  -----------#
        database.store_data(D)
        print(D.highscore_dict)
        # ---------------- DATA TO SERVER -------  -----------#
        listing = database.post_data(D)
        print('Listing is:\n', listing)

        # -------------------- INPUT -------------------- #
        start_again = Game.continue_game()

        if start_again is True:
            D.reset_data()
            continue
        else:
            break


if __name__ == "__main__":
    game()


"""
   Output of program: game_name, user_name, level_name, points, time_stamp
"""

"""
  session 00:30

"""
