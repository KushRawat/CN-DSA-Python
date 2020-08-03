def pairStar(s, si):
    if len(s) == 0 or len(s) == 1:
        return 

    s1 = " "
    s1 = s1 + s[si]
    #smallString = s[1:]
    #smallOutput =  pairStar(smallString)
    x = s[0]
    y = s[1]
    if x == y:
        s2 = s2 + "*"

    #return ('*'.join([x, y])) + pairStar(smallString)
    return pairStar(s, si + 1)
s = input()
print(pairStar(s, 0))