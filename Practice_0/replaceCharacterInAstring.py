# Program to replace a character in a string using recursion

def replaceChar(s, a, b):
    if len(s) == 0:
        return s
    smallOutput = replaceChar(s[1:], a, b)
    if s[0] == a:
        return b + smallOutput
    else:
        return s[0] + smallOutput

print(replaceChar('abc', 'b', 'x'))