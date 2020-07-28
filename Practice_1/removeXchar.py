# Problem: Remove x from string
def removeX(string): 
    #base
    if len(string) == 0:
        return string
    #hi
    smallerOutput = removeX(string[1:])
    #i
    if  string[0] == 'x':
        return smallerOutput
    else:
        return string[0] + smallerOutput

# Main
string = input()
print(removeX(string))
