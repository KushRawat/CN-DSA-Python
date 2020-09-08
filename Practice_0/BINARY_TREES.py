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

btn1 = BinaryTreeNode(1)        # creating Nodes with data
btn2 = BinaryTreeNode(2)        
btn3 = BinaryTreeNode(3)
btn4 = BinaryTreeNode(4)
btn5 = BinaryTreeNode(5)


btn1.left = btn2                # linking the nodes in a tree structure
btn1.right = btn3
btn2.left = btn4
btn2.right = btn5

printTree(btn1)