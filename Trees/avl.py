class avl:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.bal = 0
        self.depth = 0

    def rotateLeft(self):
        print("tree before rotate: ", self.left, self.val, self.right)
        top = self.right
        self.right = top.left
        top.left = self
        self = top
        print("tree before rotate: ", self.left, self.val, self.right)
        self.bal -= 1
        self.left.bal -= 2
        return True

    def rotateRight(self):
        print("tree before rotate: ", self.left, self.val, self.right)
        top = self.left
        self.left = top.right
        top.right = self
        self = top
        print("tree after rotate: ", self.left, self.val, self.right)
        self.bal += 1
        self.right.bal += 2
        return self

    def addNode(self, node):
        if node.val < self.val:
            if self.left == None:
                self.left = node
                self.bal -= 1
                self.depth += 1
            else:
                self.left.addNode(node)
                self.bal += self.left.bal
                
        else:
            if self.right == None:
                self.right = node
                self.bal += 1
                 
            else:
                self.right.addNode(node) 
                self.bal += self.right.bal  

        if self.bal < -1:
            print("balance: ", self.bal, "rotate right")
            self = self.rotateRight() 
        elif self.bal > 1:
            print("balance: ", self.bal, "rotate left")
            self.rotateLeft()    

        return True

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


x = avl(6)
y = avl(3)
z = avl(1)
a = avl(4)
x.addNode(y)
x.addNode(z)
x.addNode(a)

print("Tree: ")
y.postOrderTraversal()


