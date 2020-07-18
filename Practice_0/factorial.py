#solving factorial using recursion
def fact(x):
    if x == 0:
        return 1
    smallOutput = fact(x - 1)
    return smallOutput * x

n = int(input())
print(fact(n))