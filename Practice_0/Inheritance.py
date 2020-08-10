# Learning how inheritance works
class Vehicle:                          
    def __init__(self, color, maxSpeed): 
        self.color = color               
        self.__maxSpeed = maxSpeed       
    
    def getMaxSpeed(self):               
        return self.__maxSpeed
    
    def setMaxSpeed(self, maxSpeed):     
        self.__maxSpeed = maxSpeed

    def print(self):                      
        print("Color: ", self.color)
        print("Max Speed: ", self.__maxSpeed)

class Car(Vehicle):                     
    def __init__(self, color, maxSpeed, numGears, isConvertible): 
        super().__init__(color, maxSpeed)   
        self.numGears = numGears
        self.isConvertible = isConvertible

    def print(self):                        
        self.print() # this will lead to an error since it will be stuck in recursion, if we look carefully 
                     # we have called recursion here, and there is no base case to stop recursion

        print("Number of Gears :", self.numGears)
        print("Is Convertible :", self.isConvertible)

C = Car("Black", 299, 7, False)
C.print()    