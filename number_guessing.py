import random
import time

def generate_number():
    random_number = random.randint(1,5)
    return random_number

def input_number():
    guess_input = input("Guess the number! Input: ")
    if guess_input.isdigit():
        return guess_input
    else:
        raise TypeError("Input must be integer")

def start_again():
    guess_again = input("Guess again? (y/n) ")
    if guess_again == "y":
        guess_number()
    else:
        exit()

def guess_number():
    random_number = int(generate_number())
    print("Random Number Generated")
    time.sleep(1)
    guess_input = int(input_number())

    if guess_input < random_number:
        print("Guessed number is less than the generated number")
        start_again()

    elif guess_input > random_number:
        print("Guessed number is greater than the generated number")
        start_again()   

    else:
        print("You guessed the number!")
        start_again()

while True:
    guess_number()