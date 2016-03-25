#!/usr/bin/python
# coding: utf-8
import time


class GfxGuy:
    """ This class prints game graphics"""
    def __init__(self):
        print('GfxGuy initialized')

    def print_opening(self):
        logo_dict = {
              1: "   ===================================================== ",
              2: "   \\       Welcome to:                                 \\  ",
              3: "   /   ____  __      ___  __       __  __              /   ",
              4: "   \\  |     |__ |\\ |  |  |__ |\\ | |   |__              \\  ",
              5: "   /   ---  |__ | \\|  |  |__ | \\| |__ |__              /   ",
              6: "   \\  |___|     ___   __       __      __  __  __      \\  ",
              7: "   /           |     |__| |  ||__ |__||__ |__||__      /   ",
              8: "   \\           |___  |  \\ |__| __||  ||__ |  \\ __|     \\  ",
              9: "   ====================================================",
              10: "                                                             " }
        
        for i in range(1, 11):
            print(logo_dict[i])
            time.sleep(0.05)

    def show_string(self, D):

        level = D.level
        string_dict = {1: "\"Object-oriented programming is an exceptionally bad idea"
                          " which could only have originated in California.\" - Edsger Dijkstra",
                       2: "Good, better, best. Never let it rest. 'Til your good is"
                          " better and your better is best.",
                       3: "\"You might not think that programmers are artists, but"
                          " programming is an extremely creative profession. It's logic-based creativity.\""
                          " - John Romero",
                       4: "\"Low-level programming is good for the programmer's soul.\""
                          " - John Carmack"
                       }

        D.string = string_dict[level]
        print(D.string)

    def countdown_321(self):
        for i in (3, 2, 1):
            print("\t", i)
            time.sleep(1)

        print("\tGo!!\n")
        time.sleep(1)

    def print_stats(self, D):

        print("\n LEVEL {0} STATISTICS:                      \n"
              "                                               \n"
              "You spent {1:.2f} seconds typing on this level.\n"
              "You typed {2} wrong letter(s), and the          \n"
              " difference in lenght was {3} letter(s).        \n"
              "                                               \n"
              "TOTAL SCORE: {4}   points                       \n"
              "  Date: {5}                                     \n"
              "".format(D.level, D.clock_diff, D.wrong_letters, D.length_diff, D.points, D.time_stamp))

    def print_highscore(self, D, DB):
        level = D.level
        score_table = DB.get_sorted_highscore(D, level)

        print('                           \n'
              ' ========================= \n'
              '   HIGHSCORE: LEVEL {0})   \n'
              ' ========================= \n'
              ''.format(level))

        for tup in score_table:
            tup = str(tup)
            tup = tup.replace('(', '')
            tup = tup.replace(')', '')
            tup = tup.replace('\'', '')
            tup = '   ' + tup + ' p'
            print(tup)
            time.sleep(0.1)

        print(' ========================== \n'
              '                              ')

    def greet_user(self, D):
        name = D.user
        print("\nHello, %s " % name)




