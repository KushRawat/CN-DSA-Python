# Learning how inheritance works
class Vehicle:                          
    def __init__(self, color, maxSpeed): 
        self.color = color               
        self._maxSpeed = maxSpeed       # creating protected variable (_  )   
    
    def getMaxSpeed(self):               
        return self._maxSpeed
    
    def setMaxSpeed(self, maxSpeed):     
        self._maxSpeed = maxSpeed

    def print(self):                      
        print("Color: ", self.color)
        print("Max Speed: ", self._maxSpeed)

class Car(Vehicle):                     
    def __init__(self, color, maxSpeed, numGears, isConvertible): 
        super().__init__(color, maxSpeed)   
        self.numGears = numGears
        self.isConvertible = isConvertible

    def print(self):                        
        print("Color: ", self.color)
        print("Max Speed: ", self._maxSpeed)  
        print("Number of Gears :", self.numGears)
        print("Is Convertible :", self.isConvertible)

#C = Car("Black", 299, 7, False)
#C.print()    
#print()
V = Vehicle("Red", 299)
V.print()
print()
V._maxSpeed = 12 # possible but should not be done for protected variables
V.print()