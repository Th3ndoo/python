# abstract animal class

from abc import ABC,abstractmethod
class animal(ABC):
    def __init__(self):
        print("the animal class")

    @abstractmethod
    def move(self):
        pass


class human(animal):
    def __init__(self):
        print("the human started")
    def move(self):
        print("I can walk and run")

class snake(animal):
    def __init__(self):
        print("the snake started")
    def move(self):
        print("i can crawl")

h1 = human()
h1.move()
s1 = snake()
s1.move()
