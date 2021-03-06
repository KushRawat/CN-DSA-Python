class Complex():
    def __init__(self, x, y):
        self.real = x
        self.imag = y
        
    def add(self, otherNumber):
        self.real = str(self.real + otherNumber.real)
        self.imag = str(self.imag + otherNumber.imag)

    def multiply(self, other):
        a=self.real*other.real - self.imag*other.imag
        b= self.imag*other.real + self.real*other.imag
        self.real=str(a)
        self.imag=str(b)
    def print(self):
        print(self.real + " + " + "i" + self.imag)
        
n1 = list(int(x) for x in input().split())
n2 = list(int(x) for x in input().split())

n3 = int(input())

if n3 == 1:
    c1 = Complex(n1[0], n1[1])
    c2 = Complex(n2[0], n2[1])
    c1.add(c2)
    c1.print()
    
elif n3 == 2:
    c1 = Complex(n1[0], n1[1])
    c2 = Complex(n2[0], n2[1])
    c1.multiply(c2)
    c1.print()
    