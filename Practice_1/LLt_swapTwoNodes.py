from sys import stdin

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

# def swapNodes(head, i, j) :
def swapNodes(head, i, j):  
    if i == j:
        return head

    currNode = head
    prev = None

    firstnode = None
    secondNode = None
    firstNodePrev = None
    secondNodePrev = None

    pos = 0

    while currNode is not None:
        if pos == i:
            firstNodePrev = prev 
            firstNode = currNode
        elif pos == j:
            secondNodePrev = prev
            secondNode = currNode

        prev = currNode
        currNode = currNode.next
        pos += 1

    if firstNodePrev is not None:
        firstNodePrev.next = secondNode
    else:
        head = secondNode

    if secondNodePrev is not None:
        secondNodePrev.next = firstNode
    else:
        head = firstNode

    currentFirstNode =  secondNode.next
    secondNode.next = firstNode.next
    firstNode.next = currentFirstNode

    return head

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

def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()

#main
t = int(stdin.readline().rstrip())

while t > 0 :
    
    head = takeInput()
    i_j = stdin.readline().strip().split(" ")

    i = int(i_j[0])
    j = int(i_j[1])

    newHead = swapNodes(head, i, j)
    printLinkedList(newHead)

    t -= 1