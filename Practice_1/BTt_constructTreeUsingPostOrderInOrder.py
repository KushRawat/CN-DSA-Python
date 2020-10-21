from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


#Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



# def buildTree(postOrder, inOrder, n) :
def buildTreeHelper(postOrder, posStart, posEnd, inOrder, inStart, inEnd):
    
    if posStart > posEnd or inStart > inEnd:
        return 
    
    rootVal = postOrder[posEnd]
    root = BinaryTreeNode(rootVal)
    
    k = 0
    for i in range(inStart, inEnd + 1):
        if inOrder[i] == rootVal:
            k = i
            break
            
    root.left = buildTreeHelper(postOrder, posStart, posStart + k - inStart - 1, inOrder, inStart, k - 1)
    root.right = buildTreeHelper(postOrder, posStart + k - inStart, posEnd - 1, inOrder, k + 1, inEnd )
    
    return root

def buildTree(postOrder, inOrder, n) :
    
    posStart = 0
    posEnd = n - 1
    inStart = 0
    inEnd = n - 1
    
    return buildTreeHelper(postOrder, posStart, posEnd, inOrder, inStart, inEnd)
    





































'''-------------------------- Utility Functions --------------------------'''

def printLevelWise(root):
    if root is None :
        return

    pendingNodes = queue.Queue()
    pendingNodes.put(root)
    pendingNodes.put(None)

    while not pendingNodes.empty(): 
        frontNode = pendingNodes.get()
    
        if frontNode is None :
            print()
            
            if not pendingNodes.empty() :
                pendingNodes.put(None)
                
        else :
            print(frontNode.data, end = " ")
            
            if frontNode.left is not None :
                pendingNodes.put(frontNode.left)
                
                
            if frontNode.right is not None :
                pendingNodes.put(frontNode.right)


                

#Taking level-order input using fast I/O method
def takeInput():
    n = int(stdin.readline().strip())

    if n == 0 :
        return list(), list(), 0

    postOrder = list(map(int, stdin.readline().strip().split(" ")))
    inOrder = list(map(int, stdin.readline().strip().split(" ")))

    return postOrder, inOrder, n


# Main
postOrder, inOrder, n = takeInput()
root = buildTree(postOrder, inOrder, n)
printLevelWise(root)