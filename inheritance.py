class Person:
  def __init__(self, var1, var2):
    self.firstnum = var1
    self.secondnum = var2

  def printname(self):
    print(self.firstnum + self.secondnum)

x = Person(9,9)
x.printname()

class Child(Person):
pass
