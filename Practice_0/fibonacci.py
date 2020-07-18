# sum of fibonacci numbers using recursion
def fib(x):
    if x == 1 or x == 2:
        return 1
    fib_1 = fib(x - 1)
    fib_2 = fib(x - 2)
    output = fib_1 + fib_2
    return output

n = int(input())
print(fib(n))