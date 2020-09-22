# creating a generic tree class

class GTnode:

    def __init__(self, data):             # constructor

        self.data = data                # data to be pased
        self.children = list()          # an empty list which will be having children 

n1 = GTnode(5)
n2 = GTnode(2)
n3 = GTnode(9)
n4 = GTnode(8)
n5 = GTnode(7)
n6 = GTnode(15)
n7 = GTnode(1)

n1.children.append(2)
n1.children.append(9)
n1.children.append(8)
n1.children.append(7)

n3.children.append(15)
n3.children.append(1)

