class Student: 
    pass 

s1 = Student() 
s2 = Student()
s3 = Student()

s1.name = "Kush" # adding attribute name

s2.rollNumber = "7" # adding attribute rollNumber

s3.name = "Love" # adding attribute name
s3.rollNumber = "17" # adding attribute rollNumber

print(s1.name) # returns attribute value

print(s1.__dict__) # printing attributes and data of object s1
print(s2.__dict__) # printing attributes and data of object s2
print(s3.__dict__) # printing attributes and data of object s3

s1.testkey = "testvalue" # function 1/4 to add attribute and data together to an object 
print(s1.testkey)
print(s1.__dict__)

print(hasattr(s1, "name")) #function 2/4 to check whether the object has attribute or not

print(getattr(s1, "name")) # function 3/4 to get attribute data from the object
print(getattr(s2, "name", "cool")) # function 3/4 returns third argument in case attribute 
                                   # is not present in the object
print(getattr(s1, "testkey", "cool")) # function 3/4 does not return 3rd argument if attribute found
                                      # in object rather returns the attribute found
print(s1.__dict__)
delattr(s1, "name") # function 4/4 to delete attribute from the object
print(s1.__dict__)