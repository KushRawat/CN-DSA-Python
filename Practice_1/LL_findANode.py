
from sys import stdin

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

def length(head):
    
    count = 0
    
    while head is not None:
        count += 1
        head = head.next
    
    return count
        
def findNode(head, n) :
    
    count = 0
    curr = head
    
    for i in range(length(head)):
        if curr.data == n:
            return count
            break
        else:
            curr = curr.next
        count += 1
        
    if curr is None:    # to handle the case when n is not peresent in linked list
        return -1


#Taking Input Using Fast I/O
def takeInput() :
    head = None
    tail = None

    datas = list(map(int, stdin.readline().rstrip().split(" ")))

    i = 0
    while (i < len(datas)) and (datas[i] != -1) :
        data = datas[i]
        newNode = Node(data)

        if head is None :
            head = newNode
            tail = newNode

        else :
            tail.next = newNode
            tail = newNode

        i += 1

    return head


#to print the linked list 
def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 : 
    
    head = takeInput()
    n = int(stdin.readline().rstrip())
    print(findNode(head, n))

    t -= 1