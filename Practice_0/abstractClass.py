from abc import ABC,abstractmethod     #abc being the module, ABC the class, abstractmethod the decorator

class Automobile(ABC):
    
    def __init__(self, no_of_wheels):
        self.no_of_wheels = no_of_wheels
        print("Automobile created")

    @abstractmethod
    def start(self):                               
        print("Start of automobile called")

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def drive(self):
        pass

    @abstractmethod                   # added one more abstract method 
    def get_no_of_wheels(self):
        return self.no_of_wheels

class Car(Automobile):

    #def __init__(self, name):
     #   print("Car created")
      #  self.name = name

    def start(self):   
        super().start()              
        print("Start of car called")

    def stop(self):    
        pass

    def drive(self):
        pass

    def get_no_of_wheels(self):
        print(super().get_no_of_wheels())

class Bus(Automobile):
   # def __init__(self, name):
     #   print("Bus created")

    def start(self):
        pass
    
    def stop(self):
        pass

    def drive(self):
        pass

    def get_no_of_wheels(self):
        print(super().get_no_of_wheels())

c1 = Car(4)
c2 = Bus(16)
c1.get_no_of_wheels()
#c2.get_no_of_wheels()
    





    