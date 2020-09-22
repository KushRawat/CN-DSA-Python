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

n1 = GTnode(5)
n2 = GTnode(2)
n3 = GTnode(9)
n4 = GTnode(8)
n5 = GTnode(7)
n6 = GTnode(15)
n7 = GTnode(1)

n1.children.append(n2)
n1.children.append(n3)
n1.children.append(n4)
n1.children.append(n5)

n3.children.append(n6)
n3.children.append(n7)

printTreeDetailed(n1)