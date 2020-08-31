# Stack using array code
class Stack:

    def __init__(self):            # constructor
         self.__data = []               # private vairable so that it cannot be accessed by the user

    def push(self, item):           # push is used to add element to the stack
        self.__data.append(item)
        
    def pop(self):                      # pop is used to remove the last element
        if self.isEmpty():
            print("Hey, Stack is empty!!")
            return
        return self.__data.pop()  

    def top(self):                      # top is used to determine the most recent element
        if self.isEmpty():
            print("Hey, Stack is empty!!")
            return
        return self.__data[len(self.__data) - 1]

    def size(self):                         # size is used to know the number of elements is stack 
        return len(self.__data)

    def isEmpty(self):                       # to check if stack is empty
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