# Given a random integer array and a number x. Find and print the triplets of elements in the array which sum to x.
# While printing a triplet, print the smallest element first.
# That is, if a valid triplet is (6, 5, 10) print "5 6 10". There is no constraint that out of 5 triplets which have to be printed on 1st line. You can print triplets in any order, just be careful about the order of elements in a triplet.

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
            

def mergeSort(arr):       # will be used in tripletSum function
    if len(arr) == 0 or len(arr) == 1:
        return
    
    mid = len(arr) // 2
    a1 = arr[:mid]
    a2 = arr[mid:]
    
    mergeSort(a1)
    mergeSort(a2)
    merge(a1, a2, arr)
    
def tripletSum(arr, x):
    
    mergeSort(arr)
        
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
sum=int(input())
tripletSum(arr, sum))
