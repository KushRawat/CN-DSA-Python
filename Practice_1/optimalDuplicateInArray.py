# Given an array of integers of size n which contains numbers from 0 to n - 2. Each number is present at least once. That is, if n = 5, numbers from 0 to 3 is present in the given array at least once and one number is present twice. You need to find and return that duplicate number present in the array.
# Assume, duplicate number is always present in the array.

def MissingNumber(arr):
    sumA = sum(arr)
    sumN = ((len(arr) - 2) * (len(arr) - 1) ) // 2
    return sumA - sumN
    
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
ans=MissingNumber(arr)
print(ans)
