# This program counts number of zeroes
# in an integer using recursion
def find(n):
    if n == 0:
        return 0
    
    if n % 10 == 0:
    	return 1 + find(n // 10)
    else:
        return find(n // 10)

n = int(input())
print(find(n))