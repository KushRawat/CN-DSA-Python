# Understanding Object Classes methods

class Circle(object):        # inheriting object by default, can also be written as 
                             # class Circle():
                             # class Circle:
                             # All ways are correct
    def __init__(self,radius):
        self.radius = radius

    def __str__(self):       # one of the three object methods which lets us return any string when 
                             # print function is used (check line 15)
        return "This is a Class which takes radius as an argument"

C = Circle(5)
print(C)