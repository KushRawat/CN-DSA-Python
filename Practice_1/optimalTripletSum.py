def tripletSum(arr, x, n):
    for k in range(0, n-2):
        i = k+1
        j = n-1
        while i < j:
            if arr[i] + arr[j] + arr[k] == x:
                product = 0
                if arr[i] == arr[j]:
                    count = j-i+1
                    i = j
                    product = count*(count-1)//2
                else:
                    count1 = 1
                    count2 = 1
                    while arr[i] == arr[i+1] and i+1 < j:
                        count1+=1
                        i+=1
                    while arr[j] == arr[j-1] and j-1 > i:
                        count2+=1
                        j-=1
                    product = count1 * count2
                for a in range(0, product):
                    print(arr[k], arr[i], arr[j])
                i += 1
                j -= 1
                
            elif arr[i] + arr[j] +arr[k] > x:
                j -= 1
        
            else:
                i += 1
            
        
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
sum=int(input())
list.sort(arr)
tripletSum(arr, sum, n)
