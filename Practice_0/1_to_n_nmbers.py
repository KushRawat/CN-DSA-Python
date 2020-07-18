#print 1 to n numbers using recursion
def _1ToN(x):
    if x == 0:
        return
    _1ToN(x - 1)
    print(x)

n = int(input())
_1ToN(n)