from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

def reverseOptimal2(head):

    if head is None or head.next is None:
        return head

    smallHead = reverseOptimal2(head.next)
    tail = head.next
    tail.next = head
    head.next = None

    return smallHead

def reverseOptimal(head):  

    if head is None or head.next is None:
        return head, head

    smallHead, smallTail = reverseOptimal(head.next)
    smallTail.next = head
    head.next = None

    return smallHead, head


def reverseLinkedListRec(head) :

    if head is None:
        return None

    if head.next is None:
        return head

    smallhead = reverseLinkedListRec(head.next)

    tail = smallhead
    while tail.next is not None:
        tail = tail.next

    tail.next = head
    head.next = None

    return smallhead

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

    head = reverseOptimal2(head)
    printLinkedList(head)

    t -= 1