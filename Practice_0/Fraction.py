class Fraction:
    def __init__(self, x = 0, y = 1):
            
        if y == 0:
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
        if self.num == 0:
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

f = Fraction(10,5)                  


f.simplify()
f.print()




