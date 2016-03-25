#!/usr/bin/python
#coding: utf-8


def store_data(D):
    """
    ------------ Jonas ---"""
    # read_into_dict() creates a dictionary from file-data
    read_from_file(D, D.level)

    # Test if new score is better than old highscore
    try: 
        old_points = int(D.highscore_dict[D.user])
    except KeyError:
        old_points = 0
    
    if D.points > old_points:
        # dictionary is modified with new data
        D.highscore_dict[D.user] = [D.points]
        # The modified dictionary is written back to the file.
        write_to_file(D, D.level)
    else: 
        pass


def read_from_file(D, level):
    """
      Function will return a dictionary. 
       The dictionary will contain the entire high-score
        list for the current level like this: 
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
    while True: 
        try:
            item_pop = str(D.highscore_dict.popitem())
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

    file.close()
    return 0


def getkey(item):
    return item[0]


def get_sorted_highscore(level):
    """
      Function gets data from highscore_dict which has
       all saved data about the current level.
        Returns a sorted list of tuples, with names
         and scores from highest to lowest.
          And the lenght of said list.
         ------------------- Jonas --------------- 
    """
    
    level_data = read_into_dict(level)

    liste = []

    while True:
        try:
            getit = level_data.popitem()
            get_name = getit[0]
            get_pts = getit[1][0]
            tup = (get_name, get_pts)
            liste.append(tup)
        except KeyError:
            break

    liste_sort = sorted(liste, key=getkey, reverse=True)

    return liste_sort







