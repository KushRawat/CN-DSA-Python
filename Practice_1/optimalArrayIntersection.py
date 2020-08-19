# Optimal code for array intersection, improving the time complexity to best possible way

def mergeIntersection(arr1, arr2):  # will be used in intersection function
    i = 0
    j = 0
    
    while i < len(arr1) or j < len(arr2):
        if arr1[i] < arr2[j]:
            i = i + 1
        elif arr1[i] == arr2[j]:
            print(arr1[i])
            i = i + 1
            j = j + 1
        else:
            j = j + 1
        
def merge(a1, a2, arr):     # Will be used in  mergeSort
    i = 0
    j = 0
    k = 0
    
    while i < len(a1) and j < len(a2):
        if a1[i] < a2[j]:
            arr[k] = a1[i]
            k = k + 1
            i = i + 1
        else:
            arr[k] = a2[j]
            k = k + 1
            j = j + 1
            
    while j < len(a2):
        arr[k] = a2[j]
        k = k + 1
        j = j + 1
        
    while i < len(a1):
        arr[k] = a1[i]
        k = k + 1
        i = i + 1
            
def mergeSort(arr):      # Merge Sort using recursion
    
    if len(arr) == 0 or len(arr) == 1:
        return
    
    mid = len(arr)//2
    a1 = arr[:mid]
    a2 = arr[mid:]
    
    mergeSort(a1)
    mergeSort(a2)
    merge(a1, a2, arr)

def intersection(arr1, arr2):
    mergeSort(arr1)
    mergeSort(arr2)
    mergeIntersection(arr1, arr2)
    
# Main
n1=int(input())
arr1=list(int(i) for i in input().strip().split(' '))
n2=int(input())
arr2=list(int(i) for i in input().strip().split(' '))
intersection(arr1, arr2)
