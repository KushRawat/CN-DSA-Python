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

def removeLeaves(root):    # BT - 2

    if root is None:    # empty tree
        return None

    if root.left is None and root.right is None:    # if root is leaf
        return None

    root.left = removeLeaves(root.left)      # joining None to root's left side
    root.right = removeLeaves(root.right)
    
    return root                    # returning root with updated tree

def height(root):      # for checking isbalanced function B2

    if root is None:
        return 0

    return 1 + max(height(root.left), height(root.right))

def isBalanced(root):      # BT - 2

    if root is None:        # if tree is empty, it is balanced
        return True

    lh = height(root.left)  
    rh = height(root.right)

    if lh - rh > 1 or rh - lh > 1:
        return False

    isLeftBalanced = isBalanced(root.left)
    isRightBalanced = isBalanced(root.right)

    if isLeftBalanced and isRightBalanced:
        return True
    else:
        return False

def getHeightAndCheckBalanced(root): # BT -2 improved isBalanced

    if root is None:
        return 0, True

    lh, isLeftBalanced = getHeightAndCheckBalanced(root.left)
    rh, isRightBalanced = getHeightAndCheckBalanced(root.right)

    h = 1 + max(lh, rh)

    if lh - rh > 1 or rh - lh > 1:
        return h, False

    if isLeftBalanced and isRightBalanced:
        return h, True
    else:
        return h, False

def isBalanced2(root):             # will be used in getHeightAndCheckBalance function

    h, isRootBalanced = getHeightAndCheckBalanced(root)

    return isRootBalanced

import queue                        # BT - 2
def takeLevelWiseTreeInput():

    q = queue.Queue()

    print("Enter root")
    rootData = int(input())

    if (rootData == -1):
        return None

    root = BinaryTreeNode(rootData)

    q.put(root)

    while (not(q.empty())):

        currNode = q.get()

        print("Enter left child of", currNode.data)
        leftChildData = int(input())
        if leftChildData != -1:
            leftChild = BinaryTreeNode(leftChildData)
            currNode.left = leftChild
            q.put(leftChild)

        print("Enter right child of", currNode.data)
        rightChildData = int(input())
        if rightChildData != -1:
            rightChild = BinaryTreeNode(rightChildData)
            currNode.right = rightChild
            q.put(rightChild)
    
    return root

def nodeToRootPath(root, s):

    if root is None:
        return None

    if root.data == s:
        
        l = list()
        l.append(root.data)
        return l

    leftOutput = nodeToRootPath(root.left, s)
    if leftOutput != None:
        leftOutput.append(root.data)
        return leftOutput

    rightOutput = nodeToRootPath(root.right, s)
    if rightOutput != None:
        rightOutput.append(root.data)
        return rightOutput
    else:
        return None

root = takeLevelWiseTreeInput()
printTree(root)
print(nodeToRootPath(root, 5))

