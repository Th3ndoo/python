# abstract class and abstract method
from abc import ABC,abstractmethod

class A(ABC):
    def display(self,x):
        print("the value of x is",x)
    @abstractmethod
    def task(self):
        print("i am in the main class")

class B(A):
    def task(self):
        print("i am the inherited class")

objb = B()
objb.display(38)
objb.task()