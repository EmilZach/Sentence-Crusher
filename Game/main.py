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
from storage import StorageGuy
from data import DataGuy, InputGuy, LogicGuy
from graphics import GfxGuy


def game():
    # ------------ INITialize objects ------------- # 
    data = DataGuy()
    storage = StorageGuy()
    gfx = GfxGuy()
    Input = InputGuy() # We can't name it "input" because it is a built-in function in Python.
    logic = LogicGuy()

    # -------------- Start new_game ------------- #
    gfx.print_opening()
    Input.user_name(data)

    while True:
        # -------------------- INIT/input -------------------- #
        data.new_game_state()     # Resets data every loop - Jonas

        gfx.greet_user(data)
        Input.user_level(data)
        data.get_level_history(storage)           

        # -------------------- GRAPHICS -------------------- #
        gfx.print_highscore(data)             
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
        storage.store_data(data)

        # ---------------- DATA TO SERVER -------  -----------#
        msg = data.send_post_data()
        print('Msg from web server: ', msg)

        # -------------------- INPUT -------------------- #
        if Input.continue_game() is True:
            continue
        else:
            break


if __name__ == "__main__":
    game()


