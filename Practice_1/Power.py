# Power of numbers using recursion
def powers(a,b):
    if b == 0:
        return 1
    #if b == 1:
        return a
    #if b != 0:
    else:   
        smallOutput = powers(a, b-1)
        return a * smallOutput

a, b = input().split()
a = int(a)
b = int(b)

print(powers(a,b))
