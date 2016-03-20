import time

import graphics

def points_calc(points, clock_before, string, user_string, time_stamp, level_name):
    """ This function calculates the final score based on three
         criteria:
           - Time spent - more time less points
           - Wrong letters - more wrong, less points
           - Wrong length - more difference, less points

    :param points: Starting value of points. Default 300.
    :param clock_before: CPU-time just before the player started typing.
    :param string: This is the text the user tried to match.
    :param user_string: This is the text that is going to be evaluated
                        against string.
    :return: points - the final score is returned.
    """

    # --- Evaluate how much time the user has spent typing ---

    clock_after = time.clock()   # checks time after input
    clock_diff = clock_after - clock_before
    if clock_diff <= 5.0:
        pass
    elif clock_diff > 5.0:
        points -= (-50+(clock_diff*10))

    points = int(points)

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

    # --- Evaluate difference in length -------
    length_diff = abs(len(string) - len(user_string))
    points -= (length_diff*20)

    if points < 1:
        points = 1

    graphics.print_stats(clock_diff, wrong_letters, length_diff, points, time_stamp, level_name)

    return points
