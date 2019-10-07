# This is a code for a game in which the player must guess a random word before they run out of
# tries ("gets hanged"). It was written in the context of a 2-part python learning course, and
# is meant to introduce basic concepts of Python: strings and string manipulation, lists, tuples,
# function definition, while loops, file reading and writing.

import random

def print_presentation():
    print("*********************************")
    print("****** Welcome to Hangman! ******")
    print("*********************************")
    print("")

def load_word():
    infile = open("fruits.txt", "r", encoding="utf-8")
    words = []
    for line in infile:
        words.append(line.strip())

    infile.close()

    ind = random.randrange(0, len(words))
    secret_word = words[ind].upper()

    return secret_word

def get_user_guess():
    guess = input("Type a letter: ")
    guess = guess.strip().upper()  # no spaces, and not case sensitive, please
    return guess

def write_correct_guess(guess, right_letters, secret_word):
    index = 0
    for letter in secret_word:
        if guess == letter:
            right_letters[index] = letter
        index += 1


def print_winner_message():
    print("Congratulations, you win!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
    print("GAME OVER")


def print_loser_message(secret_word):
    print("Too bad, you were hanged!")
    print("The word was {}".format(secret_word))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")
    print("GAME OVER")

def draw_noose(errors):
    print("  _______     ")
    print(" |/      |    ")

    if(errors == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(errors == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(errors == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(errors == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(errors == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(errors == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (errors == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print("")

def run():

    print_presentation()

    secret_word = load_word()
    right_letters = ['_' for letters in secret_word]
    print(right_letters)

    errors = 0
    hanged = False
    got_right = False

    while not hanged and not got_right:

        guess = get_user_guess()

        if guess in secret_word:
            write_correct_guess(guess, right_letters, secret_word)
        else:
            errors += 1
            draw_noose(errors)

        hanged = (errors == 7)
        got_right = ('_' not in right_letters)
        print(right_letters)

    if got_right:
        print_winner_message()
    else:
        print_loser_message(secret_word)

# This prepares this python file to be executed inside another python program.
if __name__ == "__main__":
    run()