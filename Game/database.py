#!/usr/bin/python
#coding: utf-8

import requests

def store_data(D):
    """ Tasks:
        1. Read old data from file.
        2. Compare old data vs new data
        3. Store new data if old points is worse, or 
            non-existent.
    ------------------------ Jonas ---"""

    # Task 1  - (This has already been done in get_sorted_highscore())
    read_from_file(D, D.level)

    # Task 2
    try: 
        old_points = int(D.highscore_dict[D.user][0])
    except KeyError:
        old_points = 0
    
    if D.points > old_points:
        # Task 3    
        D.store_new_data()
        D.highscore_dict[D.user] = D.new_data
        write_to_file(D, D.level)

        D.new_is_better = True
    else: 
        pass


def read_from_file(D, level):
    """
      Function will return a dictionary. 
       The dictionary will contain the entire dataset
         for the current level like this: 
         { Name1: [Points, Time-stamp, Duration, level, game],
           Name2: [Points, Time-stamp, Duration, level, game] }
           ....
           ----------------------------- Jonas ----      """
    file = open('Highscorelists\level{0}.txt'.format(level), 'r')
    
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


def write_to_file(D, level):
    """
      Function writes from the modified dictionary,
       back to the file in this format: 
        name,points,Time-stamp,Duration,level,game\n
        -------------------------- Jonas ----
       """
    file = open('Highscorelists\level{0}.txt'.format(level), 'w')
    print(D.highscore_dict)
    pop_this_dict = D.highscore_dict.copy()

    while True: 
        try:
            item_pop = str(pop_this_dict.popitem())
            #Format
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

    print(D.highscore_dict)
    file.close()
    return 0


def getkey(item):
    return item[0]


def get_sorted_highscore(D, level):
    """
      Function gets data from highscore_dict which has
       all saved data about the current level.
        Returns a sorted list of tuples, with names
         and scores from highest to lowest.
          And the lenght of said list.
         ------------------- Jonas --------------- """
    
    read_from_file(D, level)
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

    liste_sort = sorted(liste, key=getkey, reverse=True)

    return liste_sort


# POST data to server
def post_data(D):
    """
    Post game data to server
    :return: listing
    """

    url = "http://127.0.0.1:5000/collect_data"

    if D.new_is_better:

        data = str(D.new_data)
        print(data)

        r = requests.post(url, data=data)

        if r:
            return r.text

    else:
        print("No data sent")






