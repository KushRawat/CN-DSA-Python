# Given a string expression, check if brackets present in the expression are balanced or not. Brackets are balanced if the bracket which opens last, closes first.
# You need to return true if it is balanced, false otherwise.
# Note: This problem was asked in initial rounds in Facebook


def checkBalanced(expr):
    
    s = []
    
    for char in expr:
        
        if char in '({[':
            
            s.append(char)
            
        elif char is ']':
            
            if (not s or s[-1] != '['):
                return False
            s.pop()
            
        elif char is '}':
            
            if (not s or s[-1] != '{'):
                return False
            s.pop()
            
        elif char is ')':
            if (not s or s[-1] != '('):
                return False
            s.pop()
            
    if (s):
        return False
    return True

exp=input()
if checkBalanced(exp):
    print('true')
else:
    print('false')

