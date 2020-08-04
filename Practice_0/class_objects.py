class Student: 
    def __init__(self, x , y): 
        self.name = x          
        self.rollNumber = y 
    
    def printStudent(self): # adding functionality to class with argument which is passed 
                            # automatically as the object
        print("My name is", self.name, "and my roll number is", self.rollNumber,) 

s1 = Student("Kush", 7)    
s1.printStudent()            #calling function printStudent
                             # We're calling this method printStudent on object s1 directly     
Student.printStudent(s1)