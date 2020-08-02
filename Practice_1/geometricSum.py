def sum(n):
    if n == 0:
        return 1
    
    a = float("%.5f" % (1 / pow(2, n)))
    
    return sum(n - 1) + a

n = int(input())
print(sum(n)) 