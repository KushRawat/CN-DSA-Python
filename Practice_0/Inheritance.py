# Learning how inheritance works
class Vehicle:                          # Parent class
    def __init__(self, color, maxSpeed): # Creating constructor, assigning properties to it
        self.color = color
        self.maxSpeed = maxSpeed

class Car(Vehicle):                     # Child Class,Inherits Vehicle
    def __init__(self, color, maxSpeed, numGears, isConvertible): # added two more properties
        super().__init__(color, maxSpeed)    # Super is used to call properties of parent function
        self.numGears = numGears
        self.isConvertible = isConvertible

    def printCar(self):                         # Creating functionality/method
        print("Color :", self.color)
        print("Max Speed :", self.maxSpeed ,"km/hr")
        print("Number of Gears :", self.numGears)
        print("Is Convertible :", self.isConvertible)

C = Car("Black", 299, 7, False)
C.printCar()