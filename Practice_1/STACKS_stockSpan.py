def stockSpan(price,n):
    
    stack = []
    
    span = []
    
    span.append(1)  # adding 1 day for 1st stock day
    
    stack.append(0) # adding position of day 1 in stock days list
	
    for i in range(1,n): # iterating through all the days' prices
        
        while price[i] > price[stack[-1]]: # comparing the 2nd day and 1st day stock price respectively
            stack.pop()				# if higher remove all postions stored in stack
            
            if len(stack) is 0:     # keep popping till stack is empty
                break
        
        if len(stack) > 0:				# if stack has positions stored
            span.append(i - stack[-1])	# then add difference bw current osition and previous position
        
        else:						# if stack is empty, this implies that current position is the highest price and needs to be appended to span
            span.append(i + 1)
            
        stack.append(i)				# append curernt positiopn to stack so that it can be compared in the nexdt oteration
            
    return span
            
n = int(input())
price = [int(ele) for ele in input().split()]
spans = stockSpan(price,n)
for ele in spans:
    print(ele,end= ' ')






