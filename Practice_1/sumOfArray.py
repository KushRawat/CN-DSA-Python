#program to calculate sum of array using recursion

def sumArray(arr):
    l = len(arr)
    if l == 0:
        return 0
    smallList = arr[1:]
    sum1 = sumArray(smallList)
    sum1 = sum1 + arr[0]
    return sum1 

from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
print(sumArray(arr))