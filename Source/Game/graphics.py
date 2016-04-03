#!/usr/bin/env python
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

    def print_string(self, data):

        level = data.level
        string_dict = {1: "\"Object-oriented programming is an exceptionally bad idea"
                          " which could only have originated in California.\" - Edsger Dijkstra",
                       2: "Good, better, best. Never let it rest. 'Til your good is"
                          " better and your better is best.",
                       3: "\"Controlling complexity is the essence of computer programming.\""
                          " - Brian Kernighan",
                       4: "\"Low-level programming is good for the programmer's soul.\""
                          " - John Carmack"
                       }

        data.lvl_string = string_dict[level]
        print(data.lvl_string)

    def countdown_321(self):
        for i in (3, 2, 1):
            print("\t", i, flush=True)
            time.sleep(1)

        print("\tGo!!\n")
        time.sleep(1)

    def print_stats(self, data):

        print("\n LEVEL {0} STATISTICS:                      \n"
              "                                               \n"
              "You spent {1:.2f} seconds typing on this level.\n"
              "You typed {2} wrong letter(s), and the          \n"
              " difference in lenght was {3} letter(s).        \n"
              "                                               \n"
              "TOTAL SCORE: {4}   points                       \n"
              "  Date: {5}                                     \n"
              "".format(data.level, data.clock_diff, data.wrong_letters, data.length_diff, data.points, data.time_stamp))

    def greet_user(self, data):
        name = data.user
        print("\nHello, %s " % name)





