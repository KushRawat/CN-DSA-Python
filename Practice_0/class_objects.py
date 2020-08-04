class Student: 
    def __init__(self): # when any object is created it will pass through __init__ function  
        self.name = "Kush" # self and created object will have the same address
        self.rollNumber = "07" # rollNumber is an attribute of self and the created object under 
                               # this class 

s1 = Student() # creating an object 
print(s1.__dict__)

s2 = Student() # creating a differnet object with a different address
print(s2.__dict__)

print(s1,s2) # Both objects have different address but same attributes  

s3 = Student("Love", 17) # this is wrong since now total number of arguments are three: self, "Love", 
                        #  17. __init__ is passing all these three arguments which is causing an error
print(s3.__dict__)