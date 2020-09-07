# Learning how to create Binary Trees

class BinaryTreeNode:

    def __init__(self, data):    # constructor
        self.data = data        # taking data as input 
        self.left = None        # initially child has nothing 
        self.right = None       # "                          "

def printTree(root):            # creating function to print tree using recursion

    if root == None:            # base case
        return

    print(root.data)            # small calculation
    printTree(root.left)        # recursion calls
    printTree(root.right)

btn1 = BinaryTreeNode(1)        # creating Nodes with data
btn2 = BinaryTreeNode(4)        
btn3 = BinaryTreeNode(7)

btn1.left = btn2                # linking the nodes in a tree structure
btn1.right = btn3

printTree(btn1)