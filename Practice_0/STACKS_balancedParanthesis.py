def isBalanced(string):

    s = []
    for char in string:
        
        if char in '({[':  # if opening brackets are present in the string add them to stack
            
            s.append(char)

        elif char is ')':
            
            if (not s or s[-1] != '('):   # if stack is empty or last element is not opening bracket since order need sto be followed for a balanced paranthesis
                return False
            s.pop()

        elif char is '}':

            if (not s or s[-1] != '{'):
                return False
            s.pop()

        elif char is ']':

            if (not s or s[-1] != '['):
                return False
            s.pop()   
    
    if (not s):      # if stack is empty, which means chars have been appended and popped return true else false 
        return True
    return False

string = input()
ans = isBalanced(string)
print(ans)