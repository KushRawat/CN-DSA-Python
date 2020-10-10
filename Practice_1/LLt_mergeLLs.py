from sys import stdin

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None



def mergeTwoSortedLinkedLists(head1,head2):
    
    FH = head1
    FT = head1
    
    while head1 is not None and head2 is not None:
        
        if head1.data < head2.data:
            
            FT.next = head2
            FT = FT.next
            head1 = head1.next
            head2 = head2.next
            
        else:
            
            FT.next = head2
            
            head1 = head1.next
            head2 = head2.next
            
            
    
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
head1 = takeInput()
head2 = takeInput()

newHead = mergeTwoSortedLinkedLists(head1, head2)
printLinkedList(newHead)