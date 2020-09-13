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

def numNodes(root):

    if root == None:            # base case
        return 0

    leftCount = numNodes(root.left)
    rightCount = numNodes(root.right)

    return 1 + leftCount + rightCount  

def largestData(root):

    if root == None: # ideally return - infinity               # base case
        return -1

    leftLargest = largestData(root.left)
    rightLargest = largestData(root.right)

    largest = max(leftLargest, rightLargest, root.data)

    return largest

def numLeafNodes(root):

    if root is None:   # to take care of the case when one side of a node is none
        return 0

    if root.left is None and root.right is None:
        return 1

    leftLeaves = numLeafNodes(root.left)
    rightLeaves = numLeafNodes(root.right)

    return leftLeaves + rightLeaves

def printDepthK(root, k):  # to find depth at K level, first level being 0

    if root is None:
        return 0

    if k == 0:
        print(root.data, end = " ")
        return

    printDepthK(root.left, k - 1)
    printDepthK(root.right, k - 1)

def printDepthKV2(root, k, d = 0):

    if root == None:
        return 

    if k == d:
        print(root.data, end = ' ')
        return

    printDepthKV2(root.left, k , d + 1)
    printDepthKV2(root.right, k , d + 1)

root = treeInput()

printDepthK(root, 2)
printDepthKV2(root, 2)
