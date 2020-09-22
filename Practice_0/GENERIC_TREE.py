# creating a generic tree class

class GTnode:

    def __init__(self, data):             # constructor

        self.data = data                # data to be passed
        self.children = list()          # an empty list which will be having children 

def printTree(root):

    if root is None:                    # not a base case but an edge case
        return

    print(root.data)

    for child in root.children:
        
        printTree(child)

def printTreeDetailed(root):

    if root is None:
        return

    print(root.data, end = ':')

    for child in root.children:

        print(child.data, end = ",")

    print()

    for child in root.children:

        printTreeDetailed(child)

def takeTreeInput():

    print("Enter root data")        # entering the root
    rootData = int(input())

    if rootData == -1:              # if root is none
        return None

    root = GTnode(rootData)             # creating node using the root

    print("Enter number of children for", rootData)             # asking for root's children
    childrenCount = int(input())

    for i in range (childrenCount):                             # iterating on number of children if any

        child = takeTreeInput()                         # calling child one by one recursively
        root.children.append(child)                     # linking the child to the root's children
    
    return root

def numNodes(root):

    if root is None:
        return 0

    count = 1

    for child in root.children:  # this handles the base case since recursion is being called only if there's a child present
        count = count + numNodes(child)

    return count

root = takeTreeInput()
printTreeDetailed(root)
print(numNodes(root))