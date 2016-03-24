#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
   Title: Sentence Crusher
   Authors: Jonas, Glenn, Emil, JanCato
   Started: 16.03.2016

"""
# --- Global modules ---
import time
import datetime
import random


# --- Local modules ---
import logics
import database

from guys import DataGuy
from guys import GameGuy
from graphics import GfxGuy

D = DataGuy()
Game = GameGuy()
Gfx = GfxGuy()


game_name = 'Sentence Crushers'

def new_game():
    # -------------------- INIT/input -------------------- #
    print("\nHello, %s " % D.user_name)
    D.level_name = Game.get_level_name()  # Data[1]

    # -------------------- GRAPHICS -------------------- #
    D.string = Gfx.get_string(D.level_name)  # Data[2]
    Gfx.print_highscore(D.level_name)              
    
    input("\n\tNow, press enter and get ready to write!")
    
    Gfx.countdown_321()
    D.clock_before = time.clock()  # checks time before input
    
    # -------------------- INPUT -------------------- #
    """ Her er det at selve spillet foregår. Spilleren får
        vist en tekstbit, som spiller skal skrive selv, så fort
         som overhodet mulig. For hvert sekund som går etter 5 sek
          så taper spilleren 10 poeng. Maksimum poengsum er 300poeng.
          -------------------------------------- Jonas --------   """
    print(D.string)
    user_string = input()
    
    # --------------------- LOGIC ----------------------- #
    time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    points, clock_diff = logics.points_calc(points, clock_before, string, user_string, time_stamp, DataGuy.level_name)

    # ---------------- DATABASE DUMP -------  -----------#
    new_list = [DataGuy.user_name, points, time_stamp, clock_diff, DataGuy.level_name, game_name]
    database.store_data(new_list)

    # ---------------- DATA TO SERVER -------  -----------#
    # Structure data to be sent to server
    data = dict(game=game_name, level=level_name, score=points, player=user_name, timestamp=time_stamp)

    # Send data to server
    listing = logics.post_data(data)

    # Print returned data from server
    print('Listing is:\n', listing)

    # -------------------- INPUT -------------------- #
    yes_or_no = input("\n  Start again? Yes?")
    if yes_or_no.upper() == "YES" or yes_or_no.upper() == "Y":
        new_game()


if __name__ == "__main__":
    Gfx.print_opening()
    user_name = input('   Please enter your user name: ')
    D.user_name = user_name.upper()  # Data[0]
    new_game()


"""
   Output of program: game_name, user_name, level_name, points, time_stamp
"""

"""
  session 00:30

"""
