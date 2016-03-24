import random


class DataGuy():

    def __init__(self):
        self.user_name = ''         # User name is a string.upper()
        self.level_name = 0         # Level between 1 - 4 
        self.points = 300           # Begins at 300 which is maximum score. 
        self.clock_before = 0.00    # Clock just before textinput 
        self.string = ''            # Text for the current level
        self.user_string = ''       # User inputted text-input
        self.time_stamp = ''        # Time stamp when user have submitted text
        self.clock_after = 0.00     # Clock when user have submitted text

        print("DataGuy initialized")


class GameGuy():

    def __init__(self):
        self.level_name = 0
        print("GameGuy initialized")

    def get_level_name(self):
        while True:
            try:
                self.level_name = int(input("Which level do you want to play; level[1, 2, 3, 4] or 5 for a random level."))
                if self.level_name == 5:
                    self.level_name = random.randrange(1,5)
                else:
                    pass  
                break

            except (ValueError, KeyError):
                print("You have to navigate using the numbers 1 to 5. Try again.")

        return self.level_name





































""" session 23:15 -      """