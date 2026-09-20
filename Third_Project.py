# Importing the required modules

import random

import time

import colorama

import pyfiglet

print()

print()

print()

print()


Number_1 = random.randint(1, 1000)

# The Rules of the Game

print("Welcome to the Number Hunt Game!")

print()

print()

time.sleep(3)

print("I have selected a random natural number between 1 and 1000.")

print()

print()

time.sleep(3)

print("Your task is to guess the number I have chosen.")

print()

print()

time.sleep(3)

print("There are two rounds in this game.")

print()

print()

time.sleep(3)

print("In the first round, you will be guessing a natural number which I have chosen, which is between 1 and 1000.")

print()

print()

time.sleep(5)

print("In the second round, you will be choosing a natural number between 1 and 1000, and I will try to guess it.")

print()

print()

time.sleep(5)

print("We will also keep track of who got the correct answer in the least number of attempts. So make sure you guess wisely!")

print()

print()

time.sleep(5)

print("Whoever guesses the number in the least number of attempts will be declared the winner!")

print()

print()

time.sleep(5)

print("Let's begin!")

print()

print()

print()

print()

time.sleep(2)

# The Game commences

Attempts_Player = 0

Done = False

while not Done:

    Guess = int(input("Please enter your guess >>> \n"))

    Attempts_Player = Attempts_Player + 1

    if Guess > Number_1:

        print("My number is smaller than your guess. Please try again.")

    if Guess < Number_1:

        print("My number is larger than your guess. Please try again.")

    if Guess == Number_1:

        print("Congratulations! You have guessed the number!")

        print("It took you", Attempts_Player, "attempts to guess the correct number.")

        Done = True

print()

print()

print()

print()

print("Now it's time for the second round! In this round, you will be choosing a natural number between 1 and 1000, and I will try to guess it.")

print()

print()

time.sleep(5)

print("Please think of a natural number between 1 and 1000, and I will try to guess it.")

print()

print()

time.sleep(3)

input("Press any key and enter when you are ready for me to start guessing!")

print()

print()

# Starting Binary Search Algorithm to guess the number

Done = False

Low = 0

High = 1000

My_Attempts = 0

while not Done:

    My_Guess = ((Low + High)//2)

    Answer = input("Is the number you are thinking of " + str(My_Guess) + "? (Y = Yes, S = Smaller than that, L = Larger than that)\n")

    My_Attempts = My_Attempts + 1

    time.sleep(3)

    if Answer.upper() == "S":

        High = My_Guess

    if Answer.upper() == "L":

        Low = My_Guess

    if Answer.upper() == "Y":

         print()

         print()

         print()

         print()
         
         print("Bingo! I have guessed the number you were thinking of!")

         print()

         print()

         time.sleep(3)

         if My_Attempts > 1:
             
             print("I took", My_Attempts, "attempts to guess it!")

         if My_Attempts == 1:

             print("I took", My_Attempts, "attempt to guess it!")

             
         
        

         Done = True


print()

print()


if My_Attempts > Attempts_Player:

    print("Congratulations! You won the Number Hunt Game!")

elif Attempts_Player > My_Attempts:

    print("You lost! Better luck next time!")

else:

    print("We both took the same number of attempts! Congratulations! The game is a draw.")

print()

print()

print()

print()

time.sleep(5)

from colorama import Fore, Style, init

init(autoreset = True)

Line_1 = pyfiglet.figlet_format("Thank You", font = "bubble")

Line_2 = pyfiglet.figlet_format("WiByte", font = "bubble")

print(Fore.MAGENTA + Style.BRIGHT + Line_1)

print(Fore.MAGENTA + Style.BRIGHT + Line_2)

print(Fore.YELLOW + Style.BRIGHT + "for teaching everything essential for this project!".center(50))
    

