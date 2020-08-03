# Write a recursive function to convert a given string into the number it represents. 
# That is input will be a numeric string that contains only numbers, you need 
# to convert the string into corresponding integer and return the answer.

def sTOi(s):
    l = len(s)
    if l == 0:
        return 0
        
    x = int(s[0])
    smallString = s[1:]
    smallOutput = (x * pow(10, l - 1)) + sTOi(smallString)
    return smallOutput
    
s = input()
print(sTOi(s))