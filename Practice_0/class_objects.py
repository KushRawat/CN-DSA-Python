class Student: 
    def __init__(self, x , y): # added 2 more arguments which will be passed when creating an object
        self.name = x          # assigned attribute to the arguments
        self.rollNumber = y  

s1 = Student("Kush", 7)        # passing the arguments which are assigned to the attributes under 
                                # __init__ function parameter
print(s1.__dict__)

s2 = Student("Love", 17) 
print(s2.__dict__)

s3 = Student("Mom", 27) 
print(s3.__dict__)