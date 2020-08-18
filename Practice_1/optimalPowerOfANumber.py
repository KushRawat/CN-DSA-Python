# Program to find power of a number using recursion in an optimal way 
# improving the time complexity

def power(x, n):
    if n == 0:
        return 1
    if x==0:
        return 0
    smallpower = power(x, n//2)
    if n % 2 == 0:
        return (smallpower * smallpower)
    else:
        return (x * smallpower * smallpower)
    

from sys import setrecursionlimit
setrecursionlimit(11000)
x, n=list(int(i) for i in input().strip().split(' '))
print(power(x, n))