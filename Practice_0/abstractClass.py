from abc import ABC,abstractmethod     #abc being the module, ABC the class, abstractmethod the decorator

class Automobile(ABC):
    
    def __init__(self):
        #self.name = "COOL"        wont work   if super().self called in line 29
        print("Automobile created")

    @abstractmethod
    def start(self):
        #self.name = "cool"        wont work  ""                                ""
        print("Start of automobile called")

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def drive(self):
        pass

class Car(Automobile):

    def __init__(self, name):
        print("Car created")
        self.name = name

    def start(self):   
        super().start()              # calling start func from abstart parent class
        print("Start of car called")

    def stop(self):    
        pass

    def drive(self):
        pass

class Bus(Automobile):
    def __init__(self, name):
        print("Bus created")

    def start(self):
        pass
    
    def stop(self):
        pass

    def drive(self):
        pass
    
c1 = Car("G-Wagon")
c1.start()
c2 = Bus("pl")






    