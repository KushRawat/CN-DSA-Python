# You have made a smartphone app and want to set its price such that the profit earned is maximised. There 
# are certain buyers who will buy your app only if their budget is greater than or equal to your price.
# You will be provided with a list of size N having budgets of buyers and you need to return the maximum 
# profit that you can earn.
# Lets say you decide that price of your app is Rs. x and there are N number of buyers. So maximum profit you 
# can earn is :
#  m * x

def maximumProfit(arr):

    arr.sort()

    count = 1
    maxCost = -1

    for i in range(len(arr) - 1, -1, -1):

        currCost = arr[i] * count

        if currCost > maxCost:
            maxCost = currCost
        
        count += 1

    return maxCost

n = int(input())
arr = [int(x) for x in input().split()]
ans = maximumProfit(arr)
print(ans)