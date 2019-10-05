from ds import *

def breadthTraversal(T):
    x = queue()
    x.enqueue(T)
    while x.length > 0:
        y = x.dequeue()
        print(y.val)
        for i in y.children:
            x.enqueue(i)
    return True

def depthTraversal(T):
    x = stack()
    x.push(T)
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

breadthTraversal(x)
print('_')
depthTraversal(x)




