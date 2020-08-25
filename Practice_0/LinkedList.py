# Learning about Linked Lists

class Node:

    def __init__(self,data):   # constructor
        self.data = data
        self.next = None

def printLL(head):             # printing the linked list
    while head is not None:
        print(str(head.data) + "->", end = "")
        head = head.next
    print("None")
    return

def takeInput():                # taking input and converting it into a linked list

    inputList = [int(ele) for ele in input().split()]
    head = None
    tail = None                   # added tail
    for currData in inputList:
        if inputList == -1:
            break
        
        newNode = Node(currData)
        if head is None:
            head = newNode 
            tail = newNode
        else:                      # shifting tail instead of traversing through the entrire list
            tail.next = newNode     
            tail = newNode
    return head 

head = takeInput()     # call for linked list formatio
printLL(head)           # call for printing the linked list
