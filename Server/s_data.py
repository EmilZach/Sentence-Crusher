#!/usr/bin/env python
# coding: utf-8


class DataGuy:
    """ This class handles data for the server"""
    def __init__(self):
        # --- Data which is going to be stored in a file -----
        self.user = ''              # User name is a string.upper()
        self.points = 300           # Begins at 300 which is maximum score. 
        self.time_stamp = ''        # Time stamp when user have submitted text
        self.clock_diff = 0.0       # Time spent typing
        self.level = 0              # Level between 1 - 4 
        self.game = ''
        self.new_data = []          # List containing all of the above

        # --- This data should be initiated by get_level_history() right after level is picked ---
        self.level_history = {}
        self.sorted_highscorelist = []

        print("Dataguy initialized")

    def make_newdata_list(self):
        self.new_data = [self.points, self.time_stamp, self.clock_diff, self.level, self.game]

