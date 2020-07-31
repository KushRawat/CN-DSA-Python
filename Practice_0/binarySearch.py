# Program to carry out binary search using recursion
def BinarySearch(a, x, si, ei):
    if si > ei: # if si == ei: , this would work too
        return -1
    mid = si + ei // 2
    if x == a[mid]:
        return mid
    elif x > mid:
        return BinarySearch(a, x, mid + 1, ei)
    else:
        return BinarySearch(a, x, si, mid -1)

print(BinarySearch([1, 2, 3, 5, 7, 8], 8, 0, 5))