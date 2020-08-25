# Program to insert data at ith position in a linked list recursively

# class
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

# print function
def printLL(head):

    while head is not None:
        print(str(head.data) + "->", end = "")
        head = head.next

    print("None")
    return

# takeinput function
def takeInput():

    inputList = [int(x) for x in input().split()]
    head = None
    tail = None

    for currData in inputList:
        if currData == -1:
            break
        
        newNode = Node(currData)
        if head is None:
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = newNode

    return head

# length function
def length(head):

    count = 0
    while head is not None:
        count += 1
        head = head.next

    return count

# insert at ith position
def insertAtI(head, i, data):
    
    if i < 0 or i > length(head):
        return head
    
    count = 0
    prev = None
    curr = head
    while count < i:
        prev = curr
        curr = curr.next
        count += 1

    newNode = Node(data)
    if prev is not None:
        prev.next = newNode
    else:
        head = newNode
    newNode.next = curr

    return head



head = takeInput()
printLL(head)
head = insertAtI(head, 0, 9)
printLL(head)
