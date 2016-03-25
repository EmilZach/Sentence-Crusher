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
from data import DataGuy, InputGuy, DatabaseGuy, LogicGuy
from graphics import GfxGuy


def game():
    # ------------ INITialize objects ------------- # 
    D = DataGuy()
    DB = DatabaseGuy()
    Gfx = GfxGuy()
    Input = InputGuy()
    Logic = LogicGuy()

    # -------------- Start new_game ------------- #
    Gfx.print_opening()
    Input.user_name(D)

    while True:
        # -------------------- INIT/input -------------------- #
        Gfx.greet_user(D)
        Input.user_level(D)           

        # -------------------- GRAPHICS -------------------- #
        Gfx.print_highscore(D, DB)             
        Input.enter_to_continue()
        
        Gfx.countdown_321()
        D.store_clock_before()
        
        # -------------------- CORE GAME -------------------- #
        Gfx.show_string(D)  
        Input.user_string(D)
        
        # --------------------- LOGIC ----------------------- #
        D.store_clock_after()
        D.store_datetime()
        Logic.calc_points(D, Gfx)

        # ---------------- DATABASE DUMP -------  -----------#
        DB.store_data(D)

        # ---------------- DATA TO SERVER -------  -----------#
        listing = DB.send_post_data(D)
        print('Listing is:\n', listing)

        # -------------------- INPUT -------------------- #
        start_again = Input.continue_game()

        if start_again is True:
            D.__init__()            # reset game data
            continue
        else:
            break


if __name__ == "__main__":
    game()


