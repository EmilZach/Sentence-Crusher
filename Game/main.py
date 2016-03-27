#!/usr/bin/env python
# coding: utf-8

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
    data = DataGuy()
    database = DatabaseGuy()
    gfx = GfxGuy()
    Input = InputGuy() # We can't name it "input" because it is a built-in function in Python.
    logic = LogicGuy()

    # -------------- Start new_game ------------- #
    gfx.print_opening()
    Input.user_name(data)

    while True:
        # -------------------- INIT/input -------------------- #
        gfx.greet_user(data)
        Input.user_level(data)           

        # -------------------- GRAPHICS -------------------- #
        gfx.print_highscore(data, database)             
        Input.enter_to_continue()
        
        gfx.countdown_321()
        data.store_clock_before()
        
        # -------------------- CORE GAME -------------------- #
        gfx.show_string(data)  
        Input.user_string(data)
        
        # --------------------- LOGIC ----------------------- #
        data.store_clock_after()
        data.store_datetime()
        logic.calc_points(data, gfx)

        # ---------------- DATABASE DUMP -------  -----------#
        database.store_data(data)

        # ---------------- DATA TO SERVER -------  -----------#
        msg = database.send_post_data(data)
        print('Msg from web server: ', msg)

        # -------------------- INPUT -------------------- #
        start_again = Input.continue_game()

        if start_again is True:
            data.restart()            # reset game data
            continue
        else:
            break


if __name__ == "__main__":
    game()


