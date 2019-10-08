class minHeap:
    def __init__(self):
        self.store = []
        self.length = len(self.store)

    def addElement(self, val):
        self.store += [val]
        self.length += 1
        if self.length > 1:
            self.heapify(self.length - 1)

        print(self.store)
        return True

    def heapify(self, idx):
        print("heapify")
        print(self.store[idx])
        if idx % 2 == 1:
            parent = (idx - 1) // 2
        else:
            parent = (idx - 2) // 2
        print(self.store[parent])

        if self.store[idx] < self.store[parent]:
            oldParent = self.store[parent]
            self.store[parent] = self.store[idx]
            self.store[idx] = oldParent

            if self.length > 3:
                self.heapify(parent)

    def removeElement(self):
        


x = minHeap()
x.addElement(1)
x.addElement(3)
x.addElement(5)
x.addElement(2)
x.addElement(4)

print(x.store)