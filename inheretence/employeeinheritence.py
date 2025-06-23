# employee inheritence

class person:
    def __init__(self,id,name):
        self.id = id
        self.name = name

    def dispperson(self):
        print(f"the employee id is {self.id}")
        print(f"the employee name is {self.name}")

class emp(person):
    def __init__(self, id, name,salary,post):
        self.salary = salary
        self.post = post
        person.__init__(self,id,name)
    def dispemp(self):
        person.dispperson(self)
        print(f"the employee salary is {self.salary}")
        print(f"the employee post is {self.post}")

emp1 = emp('101','Catherine',90000,'manager')
emp1.dispemp()
