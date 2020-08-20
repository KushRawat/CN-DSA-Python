# Optimal solution for finding the unique element in an array --> 2N + 1

def FindUnique(arr):
    x = arr[0]
    
    for i in range(1, len(arr)):
        x = x ^ arr[i]             # using xor since its associative and commutative in nature
    return x
        
    
# Main
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
unique=FindUnique(arr)
print(unique)
