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
        print("DataGuy initialized")

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

        print("Data has been reset")

    def get_datetime(self):
        self.time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def get_clock_before(self):
        self.clock_before = time.clock()

    def get_clock_after(self):
        self.clock_after = time.clock()

    def generate_newdata_list(self):
        self.new_data = [str(self.points), self.user, 
                         str(self.time_stamp), str(self.clock_diff), 
                         str(self.level), self.game]

    def generate_points(self, points):
        """ This function generates the final score based on three
             criteria:
               - Time spent - more time less points
               - Wrong letters - more wrong, less points
               - Wrong length - more difference, less points """

        points.clockdiff(self)
        points.stringlenght(self)
        points.lengthdiff(self)


class NetworkGuy:
    "This class handles talking with the server."
    def __init__(self):
        print("NetworkGuy initialized")

    def check_connection(self):
        url = "http://127.0.0.1:5000/check_link"
        try: 
            r = requests.post(url)
            if r:
                return r.text

        except requests.ConnectionError as e:
            print("\nThere is no connection to the server.\n"
                  "Your score will not be recorded.. \n")

    def send_data(self, data):
        """
        Here the new data is packaged and sent to server.
         It is important to keep the same format of the data
          throughout the program. 
           points, username, time_stamp, clock_diff, level, game
        :return: listing
        """

        url = "http://127.0.0.1:5000/store-data"

        data.generate_newdata_list()
        information = {'new_data': data.new_data}

        try:
            r = requests.post(url, data=information)
            if r:
                return r.text

        except requests.ConnectionError as e:
            print('No connection with web server.')


class PointsGuy:
    """ This class decides how much points you get"""
    def __init__(self):
        print("PointsGuy initialized")

    def clockdiff(self, data):
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

    def stringlenght(self, data):
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

    def lengthdiff(self, data):
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