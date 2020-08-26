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

# insert at ith position recursively
def insertAtIR(head, i, data):
    if i < 0:               # if position is invalid
        return head
    
    if i == 0:
        newNode = Node(data)  # creating the asked node
        newNode.next = head     # linking it with head
        return newNode       # returning the newly added linked node

    if head is None:       # in case position is greater than length of function
        return None       # written after i == 0 so that i == length case is not ignroed

    smallHead = insertAtIR(head.next, i - 1, data)
    head.next = smallHead      # joining returned newNode to rest of the list
    return head               # returning linked head to so that it can join rest of the list by recursive calls



head = takeInput()
printLL(head)
head = insertAtIR(head, 0, 9)
printLL(head)
head = insertAtIR(head, 5, 9)
printLL(head)
head = insertAtIR(head, 4, 9)
printLL(head)
head = insertAtIR(head,-1, 9)
printLL(head)
head = insertAtIR(head, 2, 9)
printLL(head)