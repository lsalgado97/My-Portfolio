# This is a code for a game in which the player must guess a random integer between 1 and 100.
# It was written in the context of a 2-part python learning course, and is meant to introduce
# basic concepts of Python: variables, logic relations, built-in types and functions, if and
# for loops, user input, program output (via print()), string formating, importing and random
# number generation.

import random

def run():
    print("********************************")
    print("** Welcome to Guess-a-Number! **")
    print("********************************")
    print("")

    points = 1000
    lost_points = 0
    total_tries = 0
    secret_number = random.randint(1, 100)

    print("Set the difficulty level")
    print("(1) Easy (2) Normal (3) Hard")
    level = int(input("Chosen level: "))

    if level == 1:
        print("You are playing on easy mode")
        total_tries = 20
    elif level == 2:
        print("You are playing on normal mode")
        total_tries = 10
    else:
        print("You are playing on hard mode")
        total_tries = 5
    print("")

    for current_round in range(1, total_tries+1):
        print("Try {} of {}".format(current_round, total_tries))  # string formatting prior to Python 3.6
        guess = int(input("Guess a number between 1 and 100: "))
        print("You guessed ", guess)

        if guess < 1 or guess > 100:
            print("You must guess between 1 and 100!")
            continue

        correct = guess == secret_number
        higher  = guess > secret_number
        smaller = guess < secret_number

        if correct:
            print("You got it right :)")
            print("You made {} points!".format(points))
            break
        else:
            if higher:
                print("You missed! Your guess is higher than the number.")
            elif smaller:
                print("You missed! Your guess is smaller than the number.")
            lost_points = abs(secret_number - guess)
            points = points - lost_points
            if current_round == total_tries:
                print("The secret number was {}, you made {} points".format(secret_number, points))

    print("GAME OVER")

# This prepares this python file to be executed inside another python program.
if __name__ == "__main__":
    run()