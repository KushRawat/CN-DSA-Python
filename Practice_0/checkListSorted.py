# Program to check if list is sorted using recursion

def isSorted(a):
    l = len(a)
    if l == 0 or l == 1:
        return True
    if a[0] > a[1]:
        return False

    smallerList = a[1:]    
    isSmallerListSorted = isSorted(smallerList) 
    return isSmallerListSorted

a = [1,2,3,40,5]
print(isSorted(a))