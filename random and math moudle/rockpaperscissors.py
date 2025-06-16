# rock paper scissors
import random
list1 = ["rock","paper","scissors"]
cg = random.choice(list1)
while True:
    user =(input("enter your choice (rock or paper or scissors)")).lower()
    if user == cg:
        print("its a tie")
        print("\n",cg)
    elif (user == 'rock' and cg == 'scissors') or (user == "paper" and cg == 'rock') or (user == 'scissors' and cg == 'paper'):
        print("you won the game!!!")
        print("\n",cg)
    else:
        print("you just lost the game!!!")
        print("\n",cg)
    choice = input("do you want to play again (y/n)")
    if choice == "n":
        break