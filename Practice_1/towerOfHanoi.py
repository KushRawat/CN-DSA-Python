# Program to solve tower of hanoi problem

def towerOfHanoi(n , a, b, c):
    if n == 1:
        print("Move 1st from", a, "to", c)
        return
    towerOfHanoi(n - 1, a, c, b)
    print("Move", n, "th from", a, "to", c)
    towerOfHanoi(n - 1, b, a, c)
    

print(towerOfHanoi(2, "s", "h", "d"))



