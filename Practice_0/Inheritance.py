# Learning how inheritance works
class Vehicle:                          
    def __init__(self, color, maxSpeed): 
        self.color = color               # public member
        self.__maxSpeed = maxSpeed       # private member (__ in front)
    
    def getMaxSpeed(self):                     # creating get function to get access to private member
        return self.__maxSpeed
    
    def setMaxSpeed(self, maxSpeed):              # creating set function
        self.__maxSpeed = maxSpeed

    def print(self):                                # Creating a print function for Vehicle properties 
                                                    # since this makes more sense
        print("Color: ", self.color)
        print("Max Speed: ", self.__maxSpeed)

class Car(Vehicle):                     
    def __init__(self, color, maxSpeed, numGears, isConvertible): 
        super().__init__(color, maxSpeed)   
        self.numGears = numGears
        self.isConvertible = isConvertible

    def printCar(self):                        
        self.print()                                # Calling print function from parent class, super().print()
                                                    # can also be used
        print("Number of Gears :", self.numGears)
        print("Is Convertible :", self.isConvertible)

C = Car("Black", 299, 7, False)
C.printCar()