#!/usr/bin/env python
# coding: utf-8


import time
import random
import datetime
import request



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

        # --- Store historic file-data in a dictionary with player-names as keys ---
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

    def send_post_data(self):
        """
        Post game data to server
        :return: listing
        """

        url = "http://127.0.0.1:5000/collect_data"

        if self.new_is_better:

            information = {}
            information['game'] = self.new_data[4]
            information['level'] = self.new_data[3]
            information['points'] = self.new_data[0]
            information['user'] = self.user
            information['time_stamp'] = self.new_data[1]

            try:
                r = requests.post(url, data=information)
                if r:
                    return r.text
            except requests.ConnectionError as e:
                print('No connection with web server.')

        else:
            print("You have a higher score already registered. No data sent")


class InputGuy:
    """ This class handles all input-events during the game """
    def __init__(self):
        print("InputGuy initialized")

    def user_name(self, data):
        user = input('   Please enter your user name: ')
        data.user = user.upper() 

    def user_level(self, data):
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

        data.level = level

    def user_string(self, data):
        data.user_string = input()

    def continue_game(self):
        yes_or_no = input("\n  Start again? Type: YES/Y")
        if yes_or_no.upper() == "YES" or yes_or_no.upper() == "Y":
            return True
        else:
            return False

    def enter_to_continue(self):
        input("\n\tNow, press enter and get ready to write!")


class LogicGuy:
    """ This class handles necessary calculations"""
    def __init__(self):
        print("LogicGuy initialized")

    def calc_points(self, data, gfx):
        """ This function calculates the final score based on three
             criteria:
               - Time spent - more time less points
               - Wrong letters - more wrong, less points
               - Wrong length - more difference, less points 
            And then it prints all the stats using graphics.print_stats()"""

        self.add_clockdiff_points(data)
        self.add_stringlen_points(data)
        self.add_lengthdiff_points(data)

        gfx.print_stats(data)

    def add_clockdiff_points(self, data):
        # --- Get data -----
        before = data.clock_before
        after = data.clock_after
        points = data.points
        diff = 0.0

        # --- Evaluate how much time the user has spent typing ---
        diff = after - before
        if diff <= 5.0:                # 5 seconds
            pass
        elif diff > 5.0:
            points -= (-50+(diff*6))
        points = int(points)          # points = float --> int
        
        # --- Return new data ---
        data.points = points
        data.clock_diff = diff

    def add_stringlen_points(self, data):
        # --- Get data ---
        lvl_string = data.lvl_string   # Level-string
        usr_string = data.user_string  # User-string
        points = data.points

        # --- Find length of shortest string ---
        if len(lvl_string) <= len(usr_string):
            short_string = len(lvl_string)
        else:
            short_string = len(usr_string)

        # --- Evaluate how many letters are wrong ----
        wrong_letters = 0
        for i in range(short_string):
            if lvl_string[i] == usr_string[i]:
                pass
            else:
                wrong_letters += 1
                points -= 2

        # --- Return new data ---
        data.points = points
        data.wrong_letters = wrong_letters

    def add_lengthdiff_points(self, data):
        # --- Get data ---
        lvl_string = data.lvl_string
        usr_string = data.user_string
        points = data.points
        diff = 0

        # --- Evaluate difference in length -------
        diff = abs(len(lvl_string) - len(usr_string))
        points -= (diff*20)
        if points < 1:
            points = 1
        
        # --- Return new data ---
        data.points = points
        data.length_diff = diff

