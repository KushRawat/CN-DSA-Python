# Program to check the first index of number if any using recursion
def checkIndex(arr, x):
    #base
    l = len(arr)
    if l == 0:
        return -1
    if arr[0] == x:
        return 0
    
    smallerList = arr[1:]
    indexPosition = checkIndex(smallerList, x)
    if indexPosition == -1:
        return -1
    else:
        return indexPosition + 1

print(checkIndex([1,2,3,3,4], 35))