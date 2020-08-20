# Given a random integer array A and a number x. Find and print the pair of elements in the array which sum to x.
# Array A can contain duplicate elements.
# While printing a pair, print the smaller element first.
# That is, if a valid pair is (6, 5) print "5 6". There is no constraint that out of 5 pairs which have to be printed in 1st line. You can print pairs in any order, just be careful about the order of elements in a pair.

def merge(arr1, arr2, arr):   # will be used in mergeSort
    i = 0
    j = 0
    k = 0
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            arr[k] = arr1[i]
            k = k + 1
            i = i + 1
        else:
            arr[k] = arr2[j]
            k = k + 1
            j = k + 1
    while i < len(arr1):
        arr[k] = arr1[i]
        k = k + 1
        i = i + 1
    while j < len(arr2):
        arr[k] = arr2[j]
        k = k + 1
        j = j + 1
            

def mergeSort(arr):       # will be used in pairSum
    if len(arr) == 0 or len(arr) == 1:
        return
    
    mid = len(arr) // 2
    a1 = arr[:mid]
    a2 = arr[mid:]
    
    mergeSort(a1)
    mergeSort(a2)
    merge(a1, a2, arr)
    
def pairSum(arr, x):
    
    mergeSort(arr)
    
    i = 0
    j = len(arr) - 1
    while i < j:
        if (arr[i] + arr[j]) < x:
            i = i + 1
        elif (arr[i] + arr[j]) > x:
            j = j - 1
        else:
            ic = arr.count(arr[i])
            jc = arr.count(arr[j])
            if ic > 1 or jc > 1:
                count = ic * jc
                return (arr[i], arr[j]) * count
            else:
            	return (arr[i], arr[j])
        i = i + 1
        j = j - 1
        
    
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
sum=int(input())
print(pairSum(arr, sum))
