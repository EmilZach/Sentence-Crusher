#!/usr/bin/env python
# coding: utf-8


import time
import random
import datetime
import requests



class DataGuy:
    """ This class handles all data for the current game """
    def __init__(self):
        # --- Data which is going to be stored in a file -----
        self.game = 'Sentence Crushers'
        self.user = ''              # User name is a string.upper()

    def new_game_state(self):
        # --- Data which is going to be stored in a file -----
        self.level = 0              # Level between 1 - 4 
        self.points = 300           # Begins at 300 which is maximum score. 
        self.clock_diff = 0.0       # Time spent typing
        self.time_stamp = ''        # Time stamp when user have submitted text
        self.new_data = []          # List containing all of the above

        # --- Data which stays only in memory ---
        self.clock_before = 0.00    # Clock just before textinput 
        self.clock_after = 0.00     # Clock when user have submitted text
        self.lvl_string = ''        # Text for the current level
        self.user_string = ''       # User inputted text-input
        self.wrong_letters = 0      # Number of lvl_string[index] != usr_string[index]
        self.length_diff = 0        # Diff in lenght between lvl_string and usr_string
        self.new_is_better = False  # If true, then data is sent to server

        # --- This data should be initiated by get_level_history() right after level is picked ---
        self.level_history = {}
        self.sorted_highscorelist = []

        print("Data has been reset")

    def get_level_history(self, storage):
        storage.read_from_file(self)
        storage.get_sorted_highscore(self)

    def store_datetime(self):
        self.time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def make_newdata_list(self):
        self.new_data = [self.points, self.time_stamp, self.clock_diff, self.level, self.game]

    def store_clock_before(self):
        self.clock_before = time.clock()

    def store_clock_after(self):
        self.clock_after = time.clock()

