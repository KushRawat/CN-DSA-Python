# Given a string expression which consists only ‘}’ and ‘{‘. The expression may not be balanced. You need to find the minimum number of bracket reversals which are required to make the expression balanced.
# Return -1 if the given expression can't be balanced.

def MBR(string):
    
    if len(string) % 2 != 0:
        return -1
    
    else:
        stack = []
        
        for i in string:
            
            if i == '{':
                stack.append(i)
            
            else:
                if (not stack):
                    stack.append(i)
                elif stack and stack[-1] == '{':
                    stack.pop()
                elif stack and stack[-1] != '{':
                    stack.append(i)
        
        count = 0
        
        for char in stack:
            
            c1 = stack.pop()
            c2 = stack.pop()
            
            if c1 == c2:
                count += 1
            
            else:
                count += 2
                
    return count


string = input()
ans  = MBR(string)
print(ans)