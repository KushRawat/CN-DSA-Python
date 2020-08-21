# Given a random integer array A and a number x. Find and print the pair of elements in the array which sum to x.
# Array A can contain duplicate elements.
# While printing a pair, print the smaller element first.
# That is, if a valid pair is (6, 5) print "5 6". There is no constraint that out of 5 pairs which have to be printed in 1st line. You can print pairs in any order, just be careful about the order of elements in a pair.

def pairSum(arr, x):
    
    arr.sort()
    
    size = len(arr)
    start = 0
    end = size - 1
    while start < end:
        if (arr[start] + arr[end]) < x:
            start += 1
        elif (arr[start] + arr[end]) > x:
            end -= 1
        else:
            product = 0
            if arr[start] == arr[end]:
                count = end - start + 1
                product = count * (count - 1) // 2
                start = end
            else:
                startCount = 1
                endCount = 1
                while start + 1 < end and arr[start + 1] == arr[start]:
                    startCount = startCount + 1
                    start = start + 1
                while start < end - 1 and arr[end - 1] == arr[end]:#
                    endCount = endCount + 1
                    end = end - 1
                product = startCount * endCount
            for j in range(product):
                print(arr[start], arr[end])
            start = start + 1
            end = end - 1
    
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
sum=int(input())
pairSum(arr, sum)