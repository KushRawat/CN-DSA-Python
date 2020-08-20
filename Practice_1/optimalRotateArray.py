from sys import stdin


def rotate(arr, n, d):
    # reversing array
    a = arr[::-1] 
    #reversing n-d elements and d elements
    a1 = a[:n - d]
    a2 = a[-d:]
    new1 = a1[::-1]
    new2 = a2[::-1]
    return new1 + new2
    
#Taking Input Using Fats I/O
def takeInput() :
    n = int(stdin.readline().rstrip())
    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


#to print the array/list 
def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ")
    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :
    
    arr, n = takeInput()
    d = int(stdin.readline().rstrip())
    rotate(arr, n, d)
    printList(arr, n)
    
    t -= 1