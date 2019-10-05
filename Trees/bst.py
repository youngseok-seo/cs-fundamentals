class bst:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def addElement(self, T):
        if T.val < self.val:
            if self.left == None:
                self.left = T
            else:
                self.left.addElement(T)
        elif T.val >= self.val:
            if self.right == None:
                self.right = T
            else:
                self.right.addElement(T)

    def preOrderTraversal(self):
        print(self.val)
        if self.left:
            self.left.preOrderTraversal()
        if self.right:
            self.right.preOrderTraversal()
        return True

    def inOrderTraversal(self):
        if self.left:
            self.left.inOrderTraversal()
        print(self.val)
        if self.right:
            self.right.inOrderTraversal()
        return True

    def postOrderTraversal(self):
        if self.left:
            self.left.postOrderTraversal()
        if self.right:
            self.right.postOrderTraversal()
        print(self.val)


x = bst(7)
y = bst(2)
z = bst(4)
a = bst(13)
b = bst(-1)
x.addElement(y)
x.addElement(z)
x.addElement(a)
x.addElement(b)
x.preOrderTraversal()
print('-')
x.inOrderTraversal()
print('-')
x.postOrderTraversal()