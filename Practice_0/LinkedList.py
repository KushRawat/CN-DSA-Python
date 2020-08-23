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
    for currData in inputList:
        if inputList == -1:
            break
        
        newNode = Node(currData)
        if head is None:
            head = newNode 
        else:
            curr = head
            while curr.next is not None:
                curr = curr.next
            curr.next = newNode

    return head 

head = takeInput()
printLL(head)
