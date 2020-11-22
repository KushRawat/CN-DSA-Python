class BinaryTreeNode():

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:

    def __init__(self):
        self.root = None
        self.numNodes = 0
    
    # Creating a helper function to call recursion
    def isPresentHelper(self, root, data):

        if root is None:
            return False

        if root.data == data:
            return True

        if root.data >= data:
            return self.isPresentHelper(root.left, data)
        else:
            return self.isPresentHelper(root.right, data)

    def isPresent(self, data):

        return self.isPresentHelper(self.root, data)

    # Creating a helper function to call recursion
    def printTreeHelper(self, root):

        if root is None:
            return 

        print(root.data, end = ":")
        
        if root.left != None:
            print(f"L:{root.left.data},", end = "")

        if root.right != None:
            print(f"R:{root.right.data}", end = "") 

        print()

        self.printTreeHelper(root.left)
        self.printTreeHelper(root.right)

    def printTree(self):
        
        self.printTreeHelper(self.root)

    # Creating a function to find the minimum node for deleteDataHelper function
    def min(self, root):

        if root is None:
            return 10000

        if root.left is None:
            return root.data  

        return self.min(root.left)

    # Creating a helper function to call recursion
    def insertHelper(self, root, data):
        
        if root is None:
            node = BinaryTreeNode(data)
            return node

        if root.data > data:
            root.left = self.insertHelper(root.left, data)
            return root

        else:
            root.right = self.insertHelper(root.right, data)
            return root

    def insert(self, data):
        
        self.numNodes += 1
        self.root = self.insertHelper(self.root, data)
    
    # Creating a helper function to call recursion
    def deleteDataHelper(self, root, data):

        if root is None:
            return False, None

        if root.data < data:

            deleted, newRightNode = self.deleteDataHelper(root.right, data)
            root.right = newRightNode
            return deleted, root

        if root.data > data:

            deleted, newLeftNode = self.deleteDataHelper(root.left, data)
            root.left = newLeftNode
            return deleted, root


        # cases when root's data == data

            # root is leaf 
        if root.left is None and root.right is None:
            return True, None
            
            # root has one child
        if root.left is None:
            return True, root.right

        if root.right is None:
            return True, root.left

            # root has two children
        replacement = self.min(root.right)
        root.data = replacement
        deleted, newRightNode = self.deleteDataHelper(root.right, replacement)
        root.right = newRightNode
        return True, root
    
    def deleteData(self, data):
        
        deleted, newRoot = self.deleteDataHelper(self.root, data)

        if deleted:
            self.numNodes -= 1
            self.root = newRoot
            return deleted  

    def count(self):
        
        return self.numNodes

b = BST()
b.insert(10)
b.insert(5)
b.insert(7)
b.insert(6)
b.insert(8)
b.insert(12)
b.insert(11)
b.insert(15)
b.printTree
print(b.count())
b.deleteData(10)
b.printTree()