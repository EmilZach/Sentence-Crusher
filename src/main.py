#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
   Title: Sentence Crusher
   Authors: Jonas, Glenn, Emil, JanCato
   Started: 16.03.2016

"""

import time
import datetime


# Timestamp
ts = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

print(ts)

game_name = 'Sentence Crusher'


def points_calc(points, clock_before, string, user_string):
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
    # --- Penalty = - 10 points for each second after 5 seconds ---

    clock_after = time.clock()   # checks time after input
    clock_diff = clock_after - clock_before
    if clock_diff <= 5.0:
        pass
    elif clock_diff > 5.0:
        points -= (-50+(clock_diff*10))

    points = int(points)
    print("Clock_diff: %.2f sekund." % clock_diff)  
    print("After clock_diff: ", points, "points")   # debug data
    
    # --- Evaluate if each letter is correct ----
    # --- Penalty 2 points for each letter wrong----
    wrong_letter = 0

    # --- Choose shortest string ---
    if len(string) <= len(user_string):
        shortest_string = len(string)
    else:
        shortest_string = len(user_string)

    # --- Use shortest string in loop below ---
    for i in range(shortest_string):
        if string[i] == user_string[i]:
            pass
        else:
            wrong_letter += 1
            points -= 2
    print("Wrong letters: ", wrong_letter)
    print("After letter check: ", points, "points")    # debug data

    # --- Evaluate difference in length -------
    # --- Penalty 20 points for each letter difference ---
    length_diff = abs(len(string) - len(user_string))
    points -= (length_diff*20)
    print("Length_diff:  ", length_diff)
    print("After length_diff: ", points, "points")   # debug data

    return points


def pick_string_level(level):

    string_dict = {1: "Object-oriented programming is an exceptionally bad idea which could only have originated in California. - Edsger Dijkstra"
                   2: "Good, better, best. Never let it rest. 'Til your good is better and your better is best."
                   3: "You might not think that programmers are artists, but programming is an extremely creative profession. It's logic-based creativity. - John Romero"
                   4: "Low-level programming is good for the programmer's soul. - John Carmack"
    

def new_game():
    global user_name
    # --------------------  INIT/input -------------------- #
        
    points = 300
    user_name = input("%s, press enter and get ready to write!" % user_name)
    
    # --------------------  GRAPHICS -------------------- #
    for i in (3, 2, 1):
        print(i)
        time.sleep(1)

    print("Go!!")
    time.sleep(1)
    clock_before = time.clock()  # checks time before input
    
    # --------------------  INPUT -------------------- #
    """ Her er det at selve spillet foregår. Spilleren får
        vist en tekstbit, som spiller skal skrive selv, så fort
         som overhodet mulig. For hvert sekund som går etter 5 sek
          så taper spilleren 10 poeng. Maksimum poengsum er 300poeng.
          -------------------------------------- Jonas --------   """
    print(string)
    user_string = input()

    # --------------------- LOGIC ----------------------- # 
    points = points_calc(points, clock_before, string, user_string)

    # --------------------  GRAPHICS -------------------- #
    print("Total points: ", int(points), "points")
    
    # --------------------  INPUT -------------------- #
    yes_or_no = input("Start again? Yes?")
    if yes_or_no.upper() == ("YES") or yes_or_no.upper() == ("Y"):
        new_game()


if __name__ == "__main__":
    user_name = input('Please enter your user name: ').upper()
    new_game()


"""
  session 12:25 - 12:40        Jonas
  session 00:25 - 01:31        Jonas
"""
