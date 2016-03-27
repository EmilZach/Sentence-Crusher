#!/usr/bin/env python
# -*- coding: utf-8 -*-


import time
import random
import datetime
import request
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
        print("Data has been reset")

    def store_datetime(self):
        self.time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def store_new_data(self):
        self.new_data = [self.points, self.time_stamp, self.clock_diff, self.level, self.game]

    def store_clock_before(self):
        self.clock_before = time.clock()

    def store_clock_after(self):
        self.clock_after = time.clock()


class InputGuy:
    """ This class handles all input-events during the game """
    def __init__(self):
        print("InputGuy initialized")

    def user_name(self, D):
        user = input('   Please enter your user name: ')
        D.user = user.upper() 

    def user_level(self, D):
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

    def user_string(self, D):
        D.user_string = input()

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

    def calc_points(self, D, Gfx):
        """ This function calculates the final score based on three
             criteria:
               - Time spent - more time less points
               - Wrong letters - more wrong, less points
               - Wrong length - more difference, less points 
            And then it prints all the stats using graphics.print_stats()"""

        self.addclockdiff_points(D)
        self.addstringlen_points(D)
        self.addlengthdiff_points(D)

        Gfx.print_stats(D)

    def addclockdiff_points(self, D):
        # --- Evaluate how much time the user has spent typing ---
        D.clock_diff = D.clock_after - D.clock_before
        if D.clock_diff <= 5.0:
            pass
        elif D.clock_diff > 5.0:
            D.points -= (-50+(D.clock_diff*6))
        D.points = int(D.points)
        return 0

    def addstringlen_points(self, D):
        # --- Choose shortest string ---
        if len(D.string) <= len(D.user_string):
            shortest_string = len(D.string)
        else:
            shortest_string = len(D.user_string)

        # --- Evaluate how many letters are wrong ----
        D.wrong_letters = 0
        for i in range(shortest_string):
            if D.string[i] == D.user_string[i]:
                pass
            else:
                D.wrong_letters += 1
                D.points -= 2
        return 0

    def addlengthdiff_points(self, D):
        # --- Evaluate difference in length -------
        D.length_diff = abs(len(D.string) - len(D.user_string))
        D.points -= (D.length_diff*20)
        if D.points < 1:
            D.points = 1
        return 0


class DatabaseGuy:
    """ This class reads from, and writes to files, and sends data to server"""
    def __init__(self):
        print("DatabaseGuy initialized")

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


    def send_post_data(self, D):
        """
        Post game data to server
        :return: listing
        """
        url = "http://127.0.0.1:5000/collect_data"

        if D.new_is_better:

            # D.new_data = [points, time_stamp, clock_diff, level, game]
            data = {}
            data['game'] = D.new_data[4]
            data['level'] = D.new_data[3]
            data['score'] = D.new_data[0]
            data['player'] = D.user
            data['timestamp'] = D.new_data[1]

            try:
                r = requests.post(url, data=data)

                if r:
                    return r.text
            except request.ConnectionError as e:
                print('No connection with web server.')

        else:
            print("No data sent")

os.path.join(os.path.dirname(__file__),('Highscorelists/level{0}.txt'))



"""
session 16:55 -  17:55
session 23:15 -  02:00    """