# creating a generic tree class

class GTnode:

    def __init__(self, data):             # constructor

        self.data = data                # data to be pased
        self.children = list()          # an empty list which will be having children 

root = GTnode(5)
print(root)