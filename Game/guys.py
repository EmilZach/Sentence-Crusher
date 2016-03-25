import time
import random
import datetime

import database

class DataGuy():

    def __init__(self):
        # --- Data which is going to be stored in file -----
        self.game = 'Sentence Crushers'
        self.user = ''              # User name is a string.upper()
        self.level = 0              # Level between 1 - 4 
        self.points = 300           # Begins at 300 which is maximum score. 
        self.clock_diff = 0.0       # Time spent typing
        self.time_stamp = ''        # Time stamp when user have submitted text

        # --- Data which is only in memory ---
        self.clock_before = 0.00    # Clock just before textinput 
        self.clock_after = 0.00     # Clock when user have submitted text
        self.string = ''            # Text for the current level
        self.user_string = ''       # User inputted text-input
        self.wrong_letters = 0      # Self explanitory
        self.new_is_better = False
        self.highscore_dict = {}    # A dictionary which a file is read to, 
                                    #      and which a file is written from.

        print("DataGuy initialized")


    def store_datetime(self):
        self.time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


class GameGuy():

    def __init__(self):
        self.level = 0
        print("GameGuy initialized")


    def get_level(self):
        while True:
            try:
                self.level = int(input("Which level do you want to play; level[1, 2, 3, 4] or 5 for a random level."))
                if self.level == 5:
                    self.level = random.randrange(1,5)
                else:
                    pass  
                break

            except (ValueError, KeyError):
                print("You have to navigate using the numbers 1 to 5. Try again.")

        return self.level





































""" session 23:15 -      """