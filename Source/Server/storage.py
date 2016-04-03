#!/usr/bin/env python
# coding: utf-8

import os

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
        # --- Get data.level_history ----
        self.read_from_file(data)
        # Task 1
        try: 
            old_points = int(data.level_history[data.user][0])
        except KeyError:
            old_points = 0
        
        if int(data.points) > old_points:
            # Task 2    
            data.level_history[data.user] = data.new_data
            self.write_to_file(data)
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
        level = str(data.level)

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
        level = str(data.level)

        # The next line is here to ensure file-path-compability on all operating systems
        os.path.join(os.path.dirname(__file__),('Highscorelists/level{0}.txt'.format(level)))
        file = open('Highscorelists/level{0}.txt'.format(level), 'w')

        updated_dict = data.level_history    
        unwanted_characters = ['[',']', '\'', ' ']
        

        for key in updated_dict:   # key: is username:
            not_write_this = ''
            write_this = ''
            not_write_this = str(key) + "," + str(updated_dict[key])
            for char in not_write_this:
                if char in unwanted_characters:
                    pass
                else:
                    write_this += char
            file.write(write_this + '\n')
        file.close()
