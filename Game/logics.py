# see http://www.python.org/peps/pep-0263.html 
import time

import graphics


def addclockdiff_points(points, clock_before):
    # --- Evaluate how much time the user has spent typing ---
    clock_after = time.clock()   # checks time after input
    clock_diff = clock_after - clock_before
    if clock_diff <= 5.0:
        pass
    elif clock_diff > 5.0:
        points -= (-50+(clock_diff*6))
    points = int(points)

    return points, clock_diff


def addstringlen_points(points, string, user_string):
    # --- Choose shortest string ---
    if len(string) <= len(user_string):
        shortest_string = len(string)
    else:
        shortest_string = len(user_string)

    # --- Evaluate how many letters are wrong ----
    wrong_letters = 0
    for i in range(shortest_string):
        if string[i] == user_string[i]:
            pass
        else:
            wrong_letters += 1
            points -= 2

    return points, wrong_letters


def addlengthdiff_points(points, string, user_string):
    # --- Evaluate difference in length -------
    length_diff = abs(len(string) - len(user_string))
    points -= (length_diff*20)
    if points < 1:
        points = 1

    return points, length_diff


def points_calc(points, clock_before, string, user_string, time_stamp, level_name):
    """ This function calculates the final score based on three
         criteria:
           - Time spent - more time less points
           - Wrong letters - more wrong, less points
           - Wrong length - more difference, less points 
        And then it prints all the stats using graphics.print_stats()"""

    points, clock_diff = addclockdiff_points(points, clock_before)
    points, wrong_letters = addstringlen_points(points, string, user_string)
    points, length_diff = addlengthdiff_points(points, string, user_string)

    graphics.print_stats(clock_diff, wrong_letters, length_diff, points, time_stamp, level_name)

    return points, clock_diff
