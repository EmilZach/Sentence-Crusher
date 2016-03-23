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
import graphics
import database


game_name = 'Sentence Crushers'


def new_game():
    # -------------------- INIT/input -------------------- #
    points = 300
    print("\nHello, %s " % user_name)
    
    # --- User picks level 1, 2, 3 or 4 ----
    while True:
        try:
            level_name = int(input("Which level do you want to play; level[1, 2, 3, 4] or 5 for a random level."))
            if level_name == 5:
                level_name = random.randrange(1,5)
            else:
                pass  
            break

        except (ValueError, KeyError):
            print("You have to navigate using the numbers 1 to 5. Try again.")

    # -------------------- GRAPHICS -------------------- #
    string = graphics.get_string(level_name)  
    graphics.print_highscore(level_name)
    
    input("\n\tNow, press enter and get ready to write!")
    
    graphics.countdown_321()
    clock_before = time.clock()  # checks time before input
    
    # -------------------- INPUT -------------------- #
    """ Her er det at selve spillet foregår. Spilleren får
        vist en tekstbit, som spiller skal skrive selv, så fort
         som overhodet mulig. For hvert sekund som går etter 5 sek
          så taper spilleren 10 poeng. Maksimum poengsum er 300poeng.
          -------------------------------------- Jonas --------   """
    print(string)
    user_string = input()
    
    # --------------------- LOGIC ----------------------- #
    time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    points, clock_diff = logics.points_calc(points, clock_before, string, user_string, time_stamp, level_name)

    # ---------------- DATABASE DUMP -------  -----------#
    new_list = [user_name, points, time_stamp, clock_diff, level_name, game_name]
    database.store_data(new_list)

    # -------------------- INPUT -------------------- #
    yes_or_no = input("\n  Start again? Yes?")
    if yes_or_no.upper() == "YES" or yes_or_no.upper() == "Y":
        new_game()


if __name__ == "__main__":
    graphics.print_opening()
    user_name = input('   Please enter your user name: ')
    user_name = user_name.upper()
    new_game()


"""
   Output of program: game_name, user_name, level_name, points, time_stamp
"""

"""
  session 00:30

"""
