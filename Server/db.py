#!/usr/bin/env python
# coding: utf-8


import time
import random
import datetime
import requests
import os


class DataGuy:
    """ This class handles all data for the current game """
    def __init__(self):
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
        # print("Data has been reset")

    def store_datetime(self):
        self.time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def store_new_data(self):
        self.new_data = [self.points, self.time_stamp, self.clock_diff, self.level, self.game]

    def store_clock_before(self):
        self.clock_before = time.clock()

    def store_clock_after(self):
        self.clock_after = time.clock()



class StorageGuy:
    """ This class reads from, and writes to files, and sends data to server"""
    def __init__(self):
        print("StorageGuy initialized")

    def store_data(self, data):
        """ Tasks:
            1. Compare old data vs new data
            2. Store new data if old points is worse, or 
                non-existent.
        ------------------------ Jonas ---"""
        # Task 1
        try: 
            old_points = int(data.level_history[data.user][0])
        except KeyError:
            old_points = 0
        
        if data.points > old_points:
            # Task 2    
            data.make_newdata_list()
            data.level_history[data.user] = data.new_data
            self.write_to_file(data)

            data.new_is_better = True
        else: 
            pass

    def read_from_file(self, data):
        """ Function will return a dictionary. 
            The dictionary will contain the entire 
             dataset for the current level like this: 
             { Name1: [Points, Time-stamp, Duration, level, game],
               Name2: [Points, Time-stamp, Duration, level, game] }
               ....
               ----------------------------- Jonas ----      """
        level = data.level

        # The next line is here to ensure file-path-compability on all operating systems
        os.path.join(os.path.dirname(__file__),('Highscorelists/level{0}.txt'.format(level)))
        file = open('Highscorelists/level{0}.txt'.format(level), 'r')
        
        while True:
            raw_line = file.readline()               # Gets a string
            line = raw_line.replace("\\n", "")       # Removes "\n" from string 
            line_list = line.split(',')              # Makes string into list
            
            if line == "":                           # This means end of file
                break
            else:
                #   DICTIONARY   [KEY]       = [VALUE1, VALUE2, VALUE3...]
                data.level_history[line_list[0]] = line_list[1:]

        file.close()

    def write_to_file(self, data):
        """Function writes from level_history, 
            which possibly contains new data,
             back to the file in this format: 
           'name,points,Time-stamp,Duration,level,game\n'
            -------------------------- Jonas ---- """
        level = data.level

        # The next line is here to ensure file-path-compability on all operating systems
        os.path.join(os.path.dirname(__file__),('Highscorelists/level{0}.txt'.format(level)))
        file = open('Highscorelists\level{0}.txt'.format(level), 'w')

        updated_dict = data.level_history    
        unwanted_characters = ['[',']', '\'', ' ']
        write_this = ''

        for key in updated_dict:   # key: is username:
            liste = []
            liste.append([key, updated_dict[key]])
            for char in str(liste):
                if char in unwanted_characters:
                    pass
                else:
                    write_this += char
            file.write(write_this)
            file.write('\n')

        file.close()

    def getkey(self, item):
        return item[1]

    def get_sorted_highscore(self, data):
        """ Function gets data from level_history which has
           all saved data about the current level.
            Returns a sorted list of tuples, with names
             and scores from highest to lowest.
             ------------------- Jonas --------------- """
        old_data = data.level_history
        liste = []
        for key in old_data:                      # Key = username
            liste.append([key, old_data[key][0]]) # Index 0 = points 

        sorted_list = sorted(liste, key=self.getkey, reverse=True)

        # --- Return new data ---
        data.sorted_highscorelist = sorted_list