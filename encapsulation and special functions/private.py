class myclass:
    __privar = 34
    def __privmeth(self):
        print("the private variable is", self.__privar)

    def hello(self):
        print("this is a public method")
        self.__privmeth()

obj1 = myclass()
obj1.__privar = 78
#obj1.__privmeth()
obj1.hello()