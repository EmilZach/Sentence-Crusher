import os

class StorageGuy:
    """ This class reads from, and writes to files, and sends data to server"""
    def __init__(self):
        print("DatabaseGuy initialized")

    def store_data(self, data):
        """ Tasks:
            1. Read old data from file.
            2. Compare old data vs new data
            3. Store new data if old points is worse, or 
                non-existent.
        ------------------------ Jonas ---"""

        # Task 1  - (This has already been done in get_sorted_highscore())
        self.read_from_file(data, data.level)

        # Task 2
        try: 
            old_points = int(data.highscore_dict[data.user][0])
        except KeyError:
            old_points = 0
        
        if data.points > old_points:
            # Task 3    
            data.store_new_data()
            data.highscore_dict[data.user] = data.new_data
            self.write_to_file(data, data.level)

            data.new_is_better = True
        else: 
            pass

    def read_from_file(self, data, level):
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
                data.highscore_dict[line_list[0]] = line_list[1:]

        file.close()

    def write_to_file(self, data, level):
        """
          Function writes from the modified dictionary,
           back to the file in this format: 
            name,points,Time-stamp,Duration,level,game\n
            -------------------------- Jonas ----
           """
        file = open('Highscorelists\level{0}.txt'.format(level), 'w')
        pop_this_dict = data.highscore_dict.copy()

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

    def get_sorted_highscore(self, data, level):
        """
          Function gets data from highscore_dict which has
           all saved data about the current level.
            Returns a sorted list of tuples, with names
             and scores from highest to lowest.
              And the lenght of said list.
             ------------------- Jonas --------------- """
        
        self.read_from_file(data, level)
        old_data = data.highscore_dict

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




os.path.join(os.path.dirname(__file__),('Highscorelists/level{0}.txt'))