# Problem ID 91, removeConsecutiveDuplicates
def removeConsecutiveDuplicates(string):
    if len(string) == 0 or len(string) == 1:
        return string
    if string[0] == string[1]:
        smallOuput = removeConsecutiveDuplicates(string[2:])
        return string[1] + smallOutput
    else:
        smallOutput = removeConsecutiveDuplicates(string[1:])
        return string[0] + smallOutput
	
    
string = input().strip()
print(removeConsecutiveDuplicates(string))
