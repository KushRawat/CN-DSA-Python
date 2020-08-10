# Understanding how multiple inheritance works

class Father:
    def print(self):
        print("Print of Father called")

class Mother:
    def print(self):
        print("Print of Mother called")

class Child(Mother, Father): # Order matters when calling function of same name
    def __init__(self, name):
        self.name = name

c = Child("kush")
c.print() # since there are two print functions being inherited, what will be printed depends on 
          # the order of parameters of child class which is inheriting (line 11)
