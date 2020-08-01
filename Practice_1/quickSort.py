def partition(a, si, ei):
    pivot = a[si]
    
    c = 0
    for i in range(si, ei + 1):
        if a[i] < pivot:
            c = c + 1
    a[si], a[si + c] = a[si + c], a[si]
    
    pivotIndex = si + c
    
    i = si
    j = ei
    while i < j:
        if a[i] < pivot:
            i =  i + 1
        elif a[j] >= pivot:
            j = j - 1
        else:
            a[i], a[j] = a[j], a[i]
            i = i + 1
            j = j - 1
    return pivotIndex
            
def quickSort(a, si, ei):
    if si >= ei:
        return
    
    pivotIndex = partition(a, si, ei)
    quickSort(a, si, pivotIndex - 1)
    quickSort(a, pivotIndex + 1, ei)
        
        

n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
quickSort(arr, 0, n-1)
print(*arr)
