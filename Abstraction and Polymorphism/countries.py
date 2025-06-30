#polymorphism

class india:
    def capital(self):
        print("the capital of india is New Delhi")
    def language(self):
        print("the widely spoken language is Hindi")
    def type(self):
        print("it's a democratic country")

class usa:
    def capital(self):
        print("the capital of usa is Washington DC")
    def language(self):
        print("the widely spoken language is english")
    def type(self):
        print("it's a democratic country")

obj1 = india()
obj2 = usa()

for i in(obj1,obj2):
    i.capital()
    i.language()
    i.type()