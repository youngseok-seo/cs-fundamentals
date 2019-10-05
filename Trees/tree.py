from ds import *

class tree:
    def __init__(self, val):
        self.val = val
        self.children = []

    def addChild(self, child):
        self. children += [child]
        return True

    def breadthTraversal(self):
        x = queue()
        x.enqueue(self)
        while x.length > 0:
            y = x.dequeue()
            print(y.val)
            for i in y.children:
                x.enqueue(i)
        return True

    def depthTraversal(self):
        x = stack()
        x.push(self)
        while x.length > 0:
            y = x.pop()
            print(y.val)
            for i in y.children:
                x.push(i)
        return True

x = tree(1)
y = tree(2)
x.addChild(y)
z = tree(3)
y.addChild(z)
a = tree(4)
x.addChild(a)

x.breadthTraversal()
print('-')
x.depthTraversal()