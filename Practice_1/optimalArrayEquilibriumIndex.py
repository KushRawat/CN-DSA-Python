# This program is to find an index i where the left sum is equal the right sum in an array

def equilibriumIndex(arr):
    totalSum = sum(arr)
    i = 0
    leftSide = 0
    while i < len(arr):
        rightSide = totalSum - leftSide - arr[i]
        if leftSide == rightSide:
            return i
        leftSide = leftSide + arr[i]
        i = i + 1
    return -1
    
n = int(input())
arr = [int(i) for i in input().strip().split()]
print(equilibriumIndex(arr))
