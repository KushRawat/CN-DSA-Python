# Prograrm to check if lost is sorted in a better way using recursion
#functionifSorted(a, si + 1)
def ifSorted(a, si): # a is array, si is starting index
    #base case
    l = len(a)
    if si == l or si == l - 1:
        return True
    if a[si] > a[si + 1]:
        return False
    #HI
    isSmallerListSorted = ifSorted(a, si + 1)
    return isSmallerListSorted
#I
print(ifSorted([1,4,3],0))