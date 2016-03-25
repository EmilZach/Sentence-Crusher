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

from guys import DataGuy
from guys import GameGuy
from guys import GfxGuy

D = DataGuy()
Gfx = GfxGuy()
Game = GameGuy()


def new_game():
    # -------------------- INIT/input -------------------- #
    print("\nHello, %s " % D.user)
    D.level = Game.get_level()           

    # -------------------- GRAPHICS -------------------- #
    Gfx.print_highscore(D, D.level)              
    
    input("\n\tNow, press enter and get ready to write!")
    
    Gfx.countdown_321()
    D.clock_before = time.clock() 
    
    # -------------------- CORE GAME -------------------- #
    Gfx.get_string(D, D.level)  
    D.user_string = input()
    
    # --------------------- LOGIC ----------------------- #
    D.store_datetime()
    logics.calc_points(D, Gfx)

    # ---------------- DATABASE DUMP -------  -----------#
    database.store_data(D)

    # ---------------- DATA TO SERVER -------  -----------#
    listing = database.post_data(D)

    # Print returned data from server
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
