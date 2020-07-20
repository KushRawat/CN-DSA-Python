def checkNumber(arr, x):
    l = len(arr)
    if l == 0:
        return True
    if x == arr[0]:
        return True
    smallList = arr[1:]
    check = checkNumber(smallList, x)
    

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
if checkNumber(arr, x):
    print('true')
else:
    print('false')
