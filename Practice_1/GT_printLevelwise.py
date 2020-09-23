class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
    def __str__(self):
        return str(self.data)

import queue 
def printLevelWiseTree(tree):

    q = queue.Queue()

    if tree is None:
        return 

    q.put(tree)

    while not(q.empty()):

        currNode = q.get()

        print(currNode.data, end = ':')

        for child in (currNode.children):

            print(child, end = ',')

            q.put(child)

        print()

def createLevelWiseTree(arr):
    root = treeNode(int(arr[0]))
    q = [root]
    size = len(arr)
    i = 1
    while i<size:
        parent = q.pop(0)
        childCount = int(arr[i])
        i += 1
        for j in range(0,childCount):
            temp = treeNode(int(arr[i+j]))
            parent.children.append(temp)
            q.append(temp)
        i += childCount
    return root

# Main
arr = list(int(x) for x in input().strip().split(' '))
tree = createLevelWiseTree(arr)
printLevelWiseTree(tree)
