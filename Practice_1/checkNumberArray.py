def checkNumber(arr, x):
    l = len(arr)
    if l == 0:
        return False
    if x == arr[0]:
        return True
    smallList = arr[1:]
    check = checkNumber(smallList, x)
    return check
    

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input()) # size of array
arr=list(int(i) for i in input().strip().split(' ')) # the array
x=int(input()) # the number to be found 
print(arr)
if checkNumber(arr, x):
    print('true')
else:
    print('false')
