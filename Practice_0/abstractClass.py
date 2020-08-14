from abc import ABC,abstractmethod     #abc being the module, ABC the class, abstractmethod the decorator

class Automobile(ABC):
    
    def __init__(self):
        print("Automobile created")

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def drive(self):
        pass

class Car(Automobile):

    #def __init__(self, name):
     #   print("Car created")
      #  self.name = name

    def start(self):   # all abstract methods need to be implemented to work 
        pass

    def stop(self):    # otherwise there will be an error
        pass

    def drive(self):
        pass

c1 = Car() # since class Car has no init funtion init of parent class Automobile will be called







    