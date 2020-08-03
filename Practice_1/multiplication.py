# This is a program to multiply two numbers using recursion
def mult(x, y):
    if y == 0 or x == 0:
        return 0
    
    smallOutput = (y - 1)
    
    j = mult(x, smallOutput)
    
    return x + j

n = int(input())
m = int(input())
print(mult(n, m))