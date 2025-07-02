# fruit quiz
import random
class fruitquiz:
    def __init__(self):
        self.fruits = {
            "apple":"red",
            "grapefruit":"orange",
            "strawberry":"red",
            "banana":"yellow",
        }
    def quiz(self):
        print("welcome to fruit quiz")
        while True:
            fruit,color = random.choice(list(self.fruits.items()))
            print("what is the color of",fruit)
            c = input("enter the color")
            if c.lower()  == color:
                print("correct answers")
            else:
                print("wrong answer")
            ch = input("do you want to continue?")
            if ch.lower() == 'n':
                break

f = fruitquiz()
f.quiz()
