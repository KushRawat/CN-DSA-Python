# Learning about Linked Lists

class Node:

    def __init__(self,data):   # constructor
        self.data = data
        self.next = None

a = Node(14)
b = Node(15)
a.next = b
print(a.data)
print(b.data)
print(a.next.data)
print(a)
print(a.next)       # same address
print(b)            # same address   
print(b.next.data)  # error