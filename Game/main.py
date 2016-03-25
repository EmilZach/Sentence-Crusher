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

D = DataGuy()
Gfx = GfxGuy()
Game = GameGuy()


def new_game():
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

    # ---------------- DATABASE DUMP -----------------#
    database.store_data(D)
    print(D.highscore_dict)

    # ---------------- DATA TO SERVER ----------------#
    listing = database.post_data(D)
    print('Listing is:\n', listing)
 
    # -------------------- INPUT -------------------- #
    yes_or_no = input("\n  Start again? Yes?")
    if yes_or_no.upper() == "YES" or yes_or_no.upper() == "Y":
        new_game()


if __name__ == "__main__":
    Gfx.print_opening()
    user = input('   Please enter your user name: ')
    D.user = user.upper()  # Data[0]
    new_game()


"""
   Output of program: game_name, user_name, level_name, points, time_stamp
"""

"""
  session 00:30

"""
