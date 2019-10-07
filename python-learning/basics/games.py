# This code is a small module to run two games, each written in a separate python code. It was
# written in the context of a python learning course, and is made to demonstrate python files
# importing. By doing this, we can run a python file inside our code.

import forca
import adivinhacao

print("*********************************")
print("**** Welcome to Salga Games! ****")
print("*********************************")
print("")
print("Games: (1) Guess-a-Number (2) Hangman")

game = int(input("Pick a game: "))

if game == 1:
    print("Let's play Guess-a-Number!")
    adivinhacao.run()
elif game == 2:
    print("Let's play Hangman!")
    forca.run()