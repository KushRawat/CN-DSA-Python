def minTree(root):

    if root is None:
        return 100000

    leftMin = minTree(root.left)
    rightMin = minTree(root.right)

    return min (leftMin, rightMin, root.data)

def maxTree(root):

    if root is None:
        return -100000

    leftMax = maxTree(root.left)
    rightMax = maxTree(root.right)

    return min (leftMax, rightMax, root.data)

def isBST(root):

    if root is None:
        return True

    leftMax = maxTree(root.left)
    rightMin = minTree(root.right)

    if leftMax < root.data or rightMin >= root.data:
        return False

    isLeftBST = isBST(root.left)
    isRightBST = isBST(root.right)
    return isLeftBST and isRightBST

def isBST2(root):
    
    if root is None:
        return 10000, -10000, True

    leftMin, leftMax, isLeftBST = isBST2(root.left)
    rightMin, rightMax, isRightBST = isBST2(root.right)

    minimum = min(leftMin, rightMin, root.data)
    maximum = max(leftMax, rightMax, root.data)

    isTreeBST = True

    if root.data <= leftMax or root.data > rightMin:
        isTreeBST = False
    
    if not(isLeftBST) or not(isRightBST):
        isTreeBST = False

    return minimum, maximum, isTreeBST

