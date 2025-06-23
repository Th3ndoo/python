# super keyword in inheritence

class Bird:
    def __init__(self):
        print("Bird is ready")
    def who(self):
        print("I am a bird")

class penguin(Bird):
    def __init__(self):
        super().__init__()
        print("penguin is ready")

    def which(self):
        Bird.who(self)
        print("I am a penguin")

p1 = penguin()
p1.which()
