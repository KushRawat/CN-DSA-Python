# Suppose you have a string, S, made up of only 'a's and 'b's. Write a recursive function that 
# checks if the string was generated using the following rules:

def checkAB(s):
    if len(s) == 1 and s[0] == "a":
        return True
    if len(s) == 2 and s[0] == "a" and s[1] == "a":
        return True
    if len(s) == 3 and s[0] == "a" and s[1] == "b" and s[2] == "b":
        return True
    if len(s) == 1 and s[0] == "b":
        return False
    
    if s[0] == "a":
        return checkAB(s[1:])
    if len(s) > 2 and s[0] == "b" and s[1] == "b":
        return checkAB(s[2:])  

s = input()
if checkAB(s):
    print("true")
else:
    print("false")