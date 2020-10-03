def split(arr, i, sum):
    
    if i == len(arr):
        
        if sum == 0:
            return True
        
        else:
            return False

    if ((arr[i] % 5) == 0):
        return split(arr, i + 1, sum + arr[i])
    
    elif ((arr[i] % 3) == 0):
        return split(arr, i + 1, sum - arr[i])

    else:
        ans1 = split(arr, i + 1, sum + arr[i])
        ans2 = split(arr, i + 1, sum - arr[i])
        return ans1 or ans2

n = int(input())
arr = [int(ele) for ele in input().split()]
ans = split(arr, 0, 0)
if ans is True:
    print('true')
else:
    print('false')