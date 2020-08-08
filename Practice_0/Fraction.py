class Fraction:
    def __init__(self, x = 0, y = 1):
            
        if y == 0: # case to taake care if denominator is zero
            y = 1  
            
        self.num = x
        self.den = y
  
    def print(self):
        if self.num == 0:
            print(0)
        elif self.den == 1:
            print(self.num)
        #elif self.den == 0:
           # print("invalid")
        else:
            print(self.num, '/' , self.den)
        
    def simplify(self):
        if self.num == 0: #case to take care if numerator is zero
            self.den == 1
            return 
        current = min(self.num, self.den)
        while current > 1:
            if self.num % current == 0 and self.den % current == 0:
                break
            current -= 1
        self.num = self.num // current
        self.den = self.den // current 
        #print(self.num, "/" , self.den)

    def add(self, otherFraction): # self is the first argument as f1 in line 39 and f2 is the 2nd arg in line 32
        newNum = otherFraction.den*self.num + otherFraction.num * self.den
        newDen = otherFraction.den * self.den
        self.num = newNum
        self.den = newDen
        self.simplify()   # calling simplify function to simplify the fraction

    def multiply(self, otherFraction):
        self.num = self.num * otherFraction.num # no need to make new var
        self.den = self.den * otherFraction.den
        self.simplify()

f1 = Fraction(3, 3)
f2 = Fraction(1, 1)                  
    
f1.multiply(f2)  # this call gives f1 as self to class function 
            # and f2 as the other argument in that class function
f1.print()


