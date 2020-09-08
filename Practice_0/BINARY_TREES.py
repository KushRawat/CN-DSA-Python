# Learning how to create Binary Trees

class BinaryTreeNode:

    def __init__(self, data):    # constructor
        self.data = data        # taking data as input 
        self.left = None        # initially child has nothing 
        self.right = None       # "                          "

def printTree(root):            # creating function to print tree using recursion

    if root == None:            # base case
        return

    print(root.data, end = ':' )            # small calculation
    
    if root.left != None:                       # to avoid error since root.left wil be None in the end
        print("L", root.left.data, end = ',')
    
    if root.right != None:
        print("R", root.right.data, end = '')
    print()
    
    printTree(root.left)        # recursion calls
    printTree(root.right)

def treeInput():            # taking data as input to create binary tree recursively

    rootData = int(input())

    if rootData == -1:      # this base case is to stop further formation of tree
        return None

    root = BinaryTreeNode(rootData)     #creating a node
    leftTree = treeInput()              # taking input for left node
    rightTree = treeInput()             # taking input for right node
    root.left = leftTree                # linking input nodes to root
    root.right = rightTree
    return root

root = treeInput()
printTree(root)