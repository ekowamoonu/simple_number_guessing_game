from ascii import numberGuessingArt
import random

print(numberGuessingArt)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100!")

difficulty = input("Choose a difficuly. Type e for easy, h for hard: ")

attempts = 0

if difficulty == 'e':
    attempts = 10
else:
    attempts = 5

print(f"You have {attempts} attempts remaining to guess the number. Good luck!")

numberToGuess = random.randint(0, 100)

while attempts > 0:
    guess = input("Make a guess: ")
    if (int(guess) > numberToGuess):
        print("Too high. Try again")
        attempts -= 1
    elif (int(guess) < numberToGuess):
        print("Too low. Try again")
        attempts -= 1
    else:
        print(f"You guessed correctly! Number is {guess}")
        break;

if attempts == 0:
    print(f"You lost. Number is {numberToGuess}")





