from sys import stdin

class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None

def reverseLinkedList(head):

    curr = head
    prev = None
    fwd = None

    while curr is not None:

        fwd = curr.next
        curr.next = prev
        prev = curr
        curr = fwd

    return prev

def isPalindrome(head):

    if head is None or head.next is None:
        return True

    #find list center
    fast = head
    slow = head

    while fast.next is not None and fast.next.next is not None:
        fast = fast.next.next
        slow = slow.next

    secondHead = slow.next
    slow.next = None
    secondHead = reverseLinkedList(secondHead)

    #compare two sublists now
    firstSubList = secondHead
    secondSubList = head

    while firstSubList is not None:
        if firstSubList.data != secondSubList.data:
            return False

        firstSubList = firstSubList.next
        secondSubList = secondSubList.next

    # Rejoin the two sublists to restore the input list to its original form
    firstSubList = head
    secondSubList = reverseLinkedList(secondHead)

    while firstSubList.next is not None:
        firstSubList = firstSubList.next

    firstSubList.next = secondSubList

    return True

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
    
    if isPalindrome(head) :
        print('true')
    else :
        print('false')
        
    t -= 1
