import time


def new_game():
    
    # --------------------  INIT -------------------- #
    string = "Lisa gikk til skolen. Tripp, tripp, tripp det sa. I den nye kjolen, trippet hun så glad."
    points = 300

    # --------------------  GRAPHICS -------------------- #
    # --- Show string ---
    input("Tast enter, og gjør deg klar til å skrive!")
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
    # --- Penalty 20 points for each letter wrong----
    wrong_letter = 0
    for i in range(len(string)):
        if string[i] == user_string[i]:
            pass
        else:
            wrong_letter += 1
            points -= 2
    print("Wrong letters: ", wrong_letter)
    print("After letter check: ", points, "points")    # debug data

    # --- Evaluate difference in length -------
    # --- Penalty 10 points for each letter difference ---
    length_diff = abs(len(string) - len(user_string))
    points -= (length_diff*10)
    print("Length_diff:  ", length_diff)
    print("After length_diff: ", points, "points")   # debug data

    # --------------------  GRAPHICS -------------------- #
    # --- Show total points -------
    print("Total points: ", int(points), "points")
    
    # --------------------  INPUT -------------------- #
    # --- Start again ----
    yes_or_no = input("Start again? Yes?")
    if yes_or_no.upper() == "YES":
        new_game()


if __name__ == "__main__":
    # Here we will insert functions that will initialize the game.
    new_game()



"""
  session 00:25  - 01:31        Jonas
"""
