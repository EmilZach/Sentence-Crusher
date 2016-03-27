#!/usr/bin/env python
# -*- coding: utf-8 -*-


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



class DatabaseGuy:
    """ This class reads from, and writes to files, and sends data to server"""

    def store_data(self, D):
        """ Tasks:
            1. Read old data from file.
            2. Compare old data vs new data
            3. Store new data if old points is worse, or 
                non-existent.
        ------------------------ Jonas ---"""

        # Task 1  - (This has already been done in get_sorted_highscore())
        self.read_from_file(D, D.level)

        # Task 2
        try: 
            old_points = int(D.highscore_dict[D.user][0])
        except KeyError:
            old_points = 0
        
        if D.points > old_points:
            # Task 3    
            D.store_new_data()
            D.highscore_dict[D.user] = D.new_data
            self.write_to_file(D, D.level)

            D.new_is_better = True
        else: 
            pass

    def read_from_file(self, D, level):
        """
          Function will return a dictionary. 
           The dictionary will contain the entire dataset
             for the current level like this: 
             { Name1: [Points, Time-stamp, Duration, level, game],
               Name2: [Points, Time-stamp, Duration, level, game] }
               ....
               ----------------------------- Jonas ----      """
        file = open('Highscorelists/level{0}.txt'.format(level), 'r')
        
        while True:
            line_cache_raw = file.readline()               # Gets a string
            line_cache = line_cache_raw.replace("\\n", "") # Removes "\n" from string 
            line_list = line_cache.split(',')              # Makes string into list
            
            if line_cache == "":                           # This means end of file
                break
            else:
                #   DICTIONARY   [KEY]       = [VALUE1, VALUE2, VALUE3...]
                D.highscore_dict[line_list[0]] = line_list[1:]

        file.close()

    def write_to_file(self, D, level):
        """
          Function writes from the modified dictionary,
           back to the file in this format: 
            name,points,Time-stamp,Duration,level,game\n
            -------------------------- Jonas ----
           """
        file = open('Highscorelists\level{0}.txt'.format(level), 'w')
        pop_this_dict = D.highscore_dict.copy()

        while True: 
            try:
                item_pop = str(pop_this_dict.popitem())
                # Format
                item_pop = item_pop.replace('"', '')
                item_pop = item_pop.replace('(', '')
                item_pop = item_pop.replace(')', '')
                item_pop = item_pop.replace('[', '')
                item_pop = item_pop.replace(']', '')
                item_pop = item_pop.replace('\'', '')
                item_pop = item_pop.replace(' ', '')
                
                file.write(item_pop)   
                file.write("\n")
            except KeyError:
                break

        file.close()
        return 0

    def getkey(self, item):
        return item[0]

    def get_sorted_highscore(self, D, level):
        """
          Function gets data from highscore_dict which has
           all saved data about the current level.
            Returns a sorted list of tuples, with names
             and scores from highest to lowest.
              And the lenght of said list.
             ------------------- Jonas --------------- """
        
        self.read_from_file(D, level)
        old_data = D.highscore_dict

        liste = []

        while True:
            try:
                getit = old_data.popitem()
                get_name = getit[0]
                get_pts = getit[1][0]
                tup = (get_name, get_pts)
                liste.append(tup)
            except KeyError:
                break

        liste_sort = sorted(liste, key=self.getkey, reverse=True)

        return liste_sort


    def list_highscore(self, D, DB):
            level = D.level
            score_table = DB.get_sorted_highscore(D, level)
            sorted_highscore_list = ''
            for tup in score_table:
                tup = str(tup)
                tup = tup.replace('(', '')
                tup = tup.replace(')', '')
                tup = tup.replace('\'', '')
                tup = '   ' + tup + ' p'
                sorted_highscore_list += tup

            return sorted_highscore_list


"""
session 16:55 -  17:55
session 23:15 -  02:00    """