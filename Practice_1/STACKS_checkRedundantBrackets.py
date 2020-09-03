def checkRedundant(string):
    
    stack = []
    count = 0
    
    for char in string:
        
        if char != ')':
            stack.append(char)
        else:
            break
            
    while char in stack != '(':
        
        char.pop()
        count += 1
        
    if count != 0:
        return True
        
		
    
string = input()
ans = checkRedundant(string)
if ans is True:
    print('true')
else:
    print('false')




