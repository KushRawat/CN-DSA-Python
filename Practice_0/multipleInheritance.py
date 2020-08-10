# Understanding how multiple inheritance works

class Father:
    def __init__(self):
        self.name = "Love"
    
    def print(self):
        print("Print of Father called")

class Mother:
    def __init__(self):
        self.name = "Kush"

    def print(self):
        print("Print of Mother called")

class Child(Mother, Father): 
    def __init__(self):
        super().__init__()
    
    def childPrint(self):
        print("The name of child is", self.name)

#c = Child()
#c.print()        
#c.childPrint()   
print(Child.mro())  # This gives the method resolution order, the order in which class and attributes will be 
                    # accessed respectively