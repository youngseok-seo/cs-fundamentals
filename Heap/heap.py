class minHeap:
    def __init__(self):
        self.store = []
        self.length = len(self.store)

    def addElement(self, val):
        print("add:", val)
        self.store += [val]
        self.length += 1
        if self.length > 1:
            self.heapify(self.length - 1)

        print(self.store)
        return True

    def heapify(self, idx):
        if idx % 2 == 1:
            parent = (idx - 1) // 2
        else:
            parent = (idx - 2) // 2

        if self.store[idx] < self.store[parent]:
            print("heapify")
            oldParent = self.store[parent]
            self.store[parent] = self.store[idx]
            self.store[idx] = oldParent

            if self.length > 3 and parent > 0:
                self.heapify(parent)

        return True

    def removeElement(self):

        head = self.store[0]
        print("remove:", head)

        tail = self.store[self.length - 1]

        self.store = [tail] + self.store[1:self.length - 1]
        self.length -= 1

        self.reheapify(0)

        return head

    def reheapify(self, idx):
        leftChild = (idx * 2) + 1
        rightChild = (idx * 2) + 2

        if (self.length - 1) == leftChild:
            if self.store[idx] > self.store[leftChild]:
                print("reheapify")
                oldParent = self.store[idx]
                self.store[idx] = self.store[leftChild]
                self.store[leftChild] = oldParent

        elif (self.length - 1) >= rightChild:
            if self.store[idx] > self.store[leftChild]:
                print("reheapify")
                oldParent = self.store[idx]
                self.store[idx] = self.store[leftChild]
                self.store[leftChild] = oldParent

                self.reheapify(leftChild)
            
            if self.store[idx] > self.store[rightChild]:
                print("reheapify")
                oldParent = self.store[idx]
                self.store[idx] = self.store[rightChild]
                self.store[rightChild] = oldParent

                self.reheapify(rightChild)

        print(self.store)

        return True

# x = minHeap()
# x.addElement(1)
# x.addElement(3)
# x.addElement(5)
# x.addElement(2)
# x.addElement(4)

# print(x.store)

# heapSorted = []
# for i in range(x.length):
#     y = x.removeElement()
#     heapSorted += [y]

# print("sorted list: ", heapSorted)
