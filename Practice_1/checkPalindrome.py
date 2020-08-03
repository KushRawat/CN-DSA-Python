def checkPal(i, si, ei):
    if si == ei:
        return True
    if i[si] != i[ei]:
        return False
    if si < ei:
        return checkPal(i, si + 1, ei  - 1)
    return True

def checkPalindrome(x):
    l = len(x)
    if l == 0:
        return True
    return checkPal(x, 0,  l -1)


s = input()
if checkPalindrome(s):
    print("true")
else:
    print("false")