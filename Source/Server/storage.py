#!/usr/bin/env python
# coding: utf-8

import os
import pickle

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
        data.level_history = self.read_from_file(data.level)
        # Task 1
        try: 
            old_points = int(data.level_history[data.user][0])
        except KeyError:
            old_points = 0
        
        if int(data.points) != old_points:
            # Task 2    
            data.level_history[data.user] = data.new_data
            self.write_to_file(data.level_history, data.level)
        else: 
            pass

    def read_from_file(self, level):
        """ Load pickle data from level-file. """
        path = self.make_path(level)
        with open(path, 'rb') as file:
              return pickle.load(file)      
        
    def write_to_file(self, record, level):
        """ Dump pickle data to level-file"""
        path = self.make_path(level)
        with open(path, 'wb') as file:
            pickle.dump(record, file)

    def make_path(self, level):
        return (os.path.join(os.path.dirname(__file__),('levelrecords/level{0}.pickle'.format(level))))
        

# Debug area
if __name__ == '__main__':

    storage = StorageGuy()
    # - The following three lines was run when the files where empty, 
    # to fill them with some form of data. 
    # dummy_dict = {'Bottomline': ['0', 'dummylevel']}
    # for level in range(1, 5):
        # storage.write_to_file(dummy_dict, level)

    for level in range(1, 5):
        print(storage.read_from_file(level))
