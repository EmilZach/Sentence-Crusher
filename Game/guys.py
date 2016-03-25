#!/usr/bin/env python
# -*- coding: utf-8 -*-


import time
import random
import datetime

import database


class DataGuy:
    """ This class handles data for the current game """
    def __init__(self):
        self.reset_data()
        print("DataGuy initialized")

    def reset_data(self):
        # --- Data which is going to be stored in a file -----
        self.game = 'Sentence Crushers'
        self.user = ''              # User name is a string.upper()
        self.level = 0              # Level between 1 - 4 
        self.points = 300           # Begins at 300 which is maximum score. 
        self.clock_diff = 0.0       # Time spent typing
        self.time_stamp = ''        # Time stamp when user have submitted text
        self.new_data = []          # List containing all of the above

        # --- Data which stays only in memory ---
        self.clock_before = 0.00    # Clock just before textinput 
        self.clock_after = 0.00     # Clock when user have submitted text
        self.string = ''            # Text for the current level
        self.user_string = ''       # User inputted text-input
        self.wrong_letters = 0      # Self explanitory
        self.new_is_better = False  # If true, then data is sent to server
        self.highscore_dict = {}    # A dictionary which a file is read to,
        #                              and which a file is written from.
        print("Data has been reset")

    def store_datetime(self):
        self.time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def store_new_data(self):
        self.new_data = [self.points, self.time_stamp, self.clock_diff, self.level, self.game]

    def store_clock_before(self):
        self.clock_before = time.clock()

    def store_clock_after(self):
        self.clock_after = time.clock()


class GameGuy:

    def __init__(self):
        print("GameGuy initialized")

    def user_input_name(self, D):
        user = input('   Please enter your user name: ')
        D.user = user.upper() 

    def user_input_level(self, D):
        while True:
            try:
                level = int(input("Which level do you want to play; level[1, 2, 3, 4] or 5 for a random level."))
                if level == 5:
                    level = random.randrange(1, 5)
                else:
                    pass  
                break

            except (ValueError, KeyError):
                print("You have to navigate using the numbers 1 to 5. Try again.")

        D.level = level

    def input_user_string(self, D):
        D.user_string = input()

    def continue_game(self):
        yes_or_no = input("\n  Start again? Type: YES/Y")
        if yes_or_no.upper() == "YES" or yes_or_no.upper() == "Y":
            return True
        else:
            return False



class GfxGuy:

    def __init__(self):
        print('GfxGuy initialized')

    def print_opening(self):
        logo_dict = {
              1: "   ===================================================== ",
              2: "   \\       Welcome to:                                 \\  ",
              3: "   /   ____  __      ___  __       __  __              /   ",
              4: "   \\  |     |__ |\\ |  |  |__ |\\ | |   |__              \\  ",
              5: "   /   ---  |__ | \\|  |  |__ | \\| |__ |__              /   ",
              6: "   \\  |___|     ___   __       __      __  __  __      \\  ",
              7: "   /           |     |__| |  ||__ |__||__ |__||__      /   ",
              8: "   \\           |___  |  \\ |__| __||  ||__ |  \\ __|     \\  ",
              9: "   ====================================================",
              10: "                                                             " }
        
        for i in range(1, 11):
            print(logo_dict[i])
            time.sleep(0.05)

    def show_string(self, D):

        level = D.level
        string_dict = {1: "\"Object-oriented programming is an exceptionally bad idea"
                          " which could only have originated in California.\" - Edsger Dijkstra",
                       2: "Good, better, best. Never let it rest. 'Til your good is"
                          " better and your better is best.",
                       3: "\"You might not think that programmers are artists, but"
                          " programming is an extremely creative profession. It's logic-based creativity.\""
                          " - John Romero",
                       4: "\"Low-level programming is good for the programmer's soul.\""
                          " - John Carmack"
                       }

        D.string = string_dict[level]
        print(D.string)

    def countdown_321(self):
        for i in (3, 2, 1):
            print("\t", i)
            time.sleep(1)

        print("\tGo!!\n")
        time.sleep(1)

    def print_stats(self, D):

        print("\n LEVEL {0} STATISTICS:                      \n"
              "                                               \n"
              "You spent {1:.2f} seconds typing on this level.\n"
              "You typed {2} wrong letter(s), and the          \n"
              " difference in lenght was {3} letter(s).        \n"
              "                                               \n"
              "TOTAL SCORE: {4}   points                       \n"
              "  Date: {5}                                     \n"
              "".format(D.level, D.clock_diff, D.wrong_letters, D.length_diff, D.points, D.time_stamp))

    def print_highscore(self, D):
        level = D.level
        score_table = database.get_sorted_highscore(D, level)

        print('                           \n'
              ' ========================= \n'
              '   HIGHSCORE: LEVEL {0})   \n'
              ' ========================= \n'
              ''.format(level))

        for tup in score_table:
            tup = str(tup)
            tup = tup.replace('(', '')
            tup = tup.replace(')', '')
            tup = tup.replace('\'', '')
            tup = '   ' + tup + ' p'
            print(tup)
            time.sleep(0.1)

        print(' ========================== \n'
              '                              ')

    def greet_user(self, D):
        name = D.user
        print("\nHello, %s " % name)



































"""
session 16:55 -  
session 23:15 -  02:00    """