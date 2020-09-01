# Program to make stacks using linked lists

# class Node:

#     def __init__(self,data):   # constructor
#         self.data = data
#         self.next = None

from LinkedList import Node

class Stack:

    def __init__(self):
        
        self.__head = None    
        self.__count = 0

    def push(self, element):
        
        newNode = Node(element)      # making a new node here
        newNode.next = self.__head      # joining new node's next to None
        self.__head = newNode 
        self.__count = self.__count + 1

    def pop(self):

        if self.isEmpty() is True:
            print("Hey, Stack is Empty!")
            return

        data = self.__head.data
        self.__head = self.__head.next
        self.__count = self.__count - 1
        return data    

    def top(self):
        
        if self.isEmpty() is True:
            print("Hey, Stack is Empty")
            return
        
        data = self.__head.data
        return data 

    def size(self):
        return self.__count 

    def isEmpty(self):
        return self.size() == 0

s = Stack()
s.push(7)
s.push(5)

print(s.top())

print(s.isEmpty())

print(s.pop())
print(s.pop())
print(s.pop())
s.pop()

print(s.size())

print(s.isEmpty())

s.top()

s.push(1)
s.push(2)

print(s.size())

print(s.isEmpty())

while s.isEmpty() is False:
    print(s.pop())

print(s.size())

print(s.top())