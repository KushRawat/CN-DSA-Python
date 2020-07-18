# print n to 1 numbers using recursion
def nTo1(x):
    if x == 0:
        return 
    print(x)
    nTo1(x - 1)

n = int(input())    
nTo1(n)