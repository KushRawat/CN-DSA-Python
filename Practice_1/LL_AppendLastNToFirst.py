# You have been given a singly linked list of integers along with an integer 'N'. Write a function to append the last 'N' nodes towards the front of the singly linked list and returns the new head to the list.


from sys import stdin

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None


def length(head):
    
    count = 0
    while head is not None:
        head = head.next
        count += 1
        
    return count

def appendLastNToFirst(head, n) :
    
    curr = head
    count = 1
    i = length(head) - n
    if i==0:                    # when length and n is same 
        return head

    while count < i:
        curr = curr.next
        count= count + 1
    
    if curr is None: 		 # in case of empty linked list 
        return head
    
    h2 = curr  
    
    while(curr.next is not None): 
        curr = curr.next
    
    curr.next = head    # linking head to last node
    head = h2.next
    h2.next = None
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

    head = appendLastNToFirst(head, n)
    printLinkedList(head)

    t -= 1 