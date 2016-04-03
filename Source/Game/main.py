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
from data import DataGuy, InputGuy, PointsGuy, NetworkGuy
from graphics import GfxGuy


def game():
    # ------------ INITialize objects ------------- # 
    data = DataGuy()
    network = NetworkGuy()
    graphics = GfxGuy()
    Input = InputGuy() # We can't name it "input" because it is a built-in function in Python.
    points = PointsGuy()

    # -------------- Start new_game ------------- #
    graphics.print_opening()
    Input.user_name(data)

    network.check_connection()

    while True:
        # -------------------- INIT/input -------------------- #
        data.new_game_state()     # Resets data every loop - Jonas

        graphics.greet_user(data)
        Input.user_level(data)         

        # -------------------- GRAPHICS -------------------- #          
        Input.enter_to_continue()
        
        graphics.countdown_321()
        data.get_clock_before()
        
        # -------------------- CORE GAME -------------------- #
        graphics.print_string(data)  
        Input.user_string(data)
        
        # --------------------- LOGIC ----------------------- #
        data.get_clock_after()
        data.get_datetime()
        data.generate_points(points)

        # ---------------- DATA TO SERVER -------  -----------#
        msg = network.send_data(data)

        # -------------------- GRAPHICS/INPUT -------------------- #
        print('Msg from web server: ', msg)
        graphics.print_stats(data)

        if Input.continue_game() is True:
            continue
        else:
            break


if __name__ == "__main__":
    game()


