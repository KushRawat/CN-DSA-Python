# Program to check last index of a number using recursion in a better way
def checkIndex(arr, x, si):
    #base
    l = len(arr):
    if l == si:
        return -1
    #hi
    smallerListOutput = checkIndex(arr, x, si + 1)
    #i
    if smallerListOutput != -1:
        return smallerListOutput
    else:
        if arr[si] == x:
            return si
        else:
            return -1

print(checkIndex([1, 2, 3], 3, 0))
