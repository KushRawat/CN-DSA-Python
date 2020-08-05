class Fraction:
    def __init__(self, x = 0, y = 1): # assigning default values or default parameters
        self.num = x
        self.den = y

f = Fraction(2, 3)                  # created a function with two integer values
print(f.__dict__)

f1 = Fraction()                     # created a function wuth no values
print(f1.__dict__)

f2 = Fraction(2)                       # created a function with one value
print(f2.__dict__)

f3 = Fraction(y = 5)                # created a function with 
print(f3.__dict__)