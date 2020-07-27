# Program to check the first index of number if any using recursion in a better way
from sys import setrecursionlimit
setrecursionlimit(20000)

def checkIndex(arr, x, si):
    #base case
    l = len(arr)
    if si == l:
        return -1
    if arr[si] == x:
        return si
    #IH
    smallerList = checkIndex(arr, x, si + 1)
    return smallerList
#I
print(checkIndex([1,2,3,4,5], 3, 0))