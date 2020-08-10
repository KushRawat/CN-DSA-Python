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
        super().print()  # super() here helps rectifying the mistake when we call self.print()
                         # It calls print function from its parent class
        print("Number of Gears :", self.numGears)
        print("Is Convertible :", self.isConvertible)

C = Car("Black", 299, 7, False)
C.print()    