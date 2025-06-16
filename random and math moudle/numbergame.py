# number game 
import random

cg = random.randint(1,10)

while True:
    n = int(input("enter a number"))
    if n == cg:
        print("Congratulations, your guess is right")
        break
    else:
        print("guessed wrongly\n Try again \n")