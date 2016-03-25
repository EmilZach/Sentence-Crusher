#!/usr/bin/python
#coding: utf-8

import time
import requests

import graphics
import guys



def addclockdiff_points(D):
    # --- Evaluate how much time the user has spent typing ---
    D.clock_after = time.clock()   # checks time after input
    D.clock_diff = D.clock_after - D.clock_before
    if D.clock_diff <= 5.0:
        pass
    elif D.clock_diff > 5.0:
        D.points -= (-50+(D.clock_diff*6))
    D.points = int(D.points)
    return 0


def addstringlen_points(D):
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


def addlengthdiff_points(D):
    # --- Evaluate difference in length -------
    D.length_diff = abs(len(D.string) - len(D.user_string))
    D.points -= (D.length_diff*20)
    if D.points < 1:
        D.points = 1
    return 0


def calc_points(D, Gfx):
    """ This function calculates the final score based on three
         criteria:
           - Time spent - more time less points
           - Wrong letters - more wrong, less points
           - Wrong length - more difference, less points 
        And then it prints all the stats using graphics.print_stats()"""

    addclockdiff_points(D)
    addstringlen_points(D)
    addlengthdiff_points(D)

    Gfx.print_stats(D)

    return 0


# POST data to server
def post_data(D):
    """
    Post game data to server
    :return: listing
    """

    url = "http://127.0.0.1:5000/collect_data"

    data = data

    r = requests.post(url, data=data)

    if r:
        return r.text
