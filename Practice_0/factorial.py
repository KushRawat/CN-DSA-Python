#solving factorial using recursion
import sys # increasing recursion depth limit by importing sys library
sys.setrecursionlimit(2000)

def fact(x):
    if x == 0:
        return 1
    smallOutput = fact(x - 1)
    return smallOutput * x

n = int(input())
print(fact(n))