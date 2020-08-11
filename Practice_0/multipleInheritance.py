# Understanding how multiple inheritance works

class Father:
    def __init__(self):
        self.name = "Love"
        super().__init__()      # confusion
    
    def print(self):
        print("Print of Father called")

class Mother:
    def __init__(self):
        self.name = "Kush"
        super().__init__()    # confusion

    def print(self):
        print("Print of Mother called")

class Child(Mother, Father): 
    def __init__(self):
        super().__init__()
    
    def print(self):
        print("The name of child is", self.name)

c = Child()
c.print()        
#c.childPrint()   
print(Child.mro())  