#Sum of n natural numbers using recursion
def sum(x):
    if x == 1:
        return 1
    smallOutput = sum(x - 1)
    return x + smallOutput


n = int(input())
print(sum(n)) 