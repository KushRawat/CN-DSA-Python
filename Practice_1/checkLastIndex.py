def lastIndex(arr, x):
	# base
    l = len(arr)
    if l == 0:
        return -1
    smallerList = arr[1:]
    smallerListOutput = lastIndex(smallerList, x)
    # I
    if smallerListOutput != -1:
        return smallerListOutput + 1
    else:
        if arr[0] == x:
            return 0
        else:
            return -1
        
n = int(input()) # size of array
arr = list(int(x) for x in input().strip().split())
x = int(input())

print(lastIndex(arr, x))
