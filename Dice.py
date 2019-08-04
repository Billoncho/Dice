# Dice.py
# Billy Ridgeway
# Simulates rolling 5 dice.

import random       # Imports the random library.
keep_going = True   # Set the variable to true.

# Creates a while loop that will simulate rolling 5 dice and showing the
# user the results. The game will continue until the user presses any key
# other than Enter.
while keep_going:
    dice = [0, 0, 0, 0, 0]              # Sets all the dice to zero.
    for i in range(5):                  # Rolls the dice.
        dice[i] = random.randint(1, 6)  # Assigns a random number to each di.
    print("You rolled:", dice, ".")     # Prints the user's dice.
    answer = input("Keep going?")       # Asks the user to continue or quit.
    keep_going = (answer == "")         # Evaluates the user's response.
