import ds

class vertex:
    def __init__(self, val):
        self.visited = False
        self.processed = False
        self.val = val


class graph:
    def __init__(self):
        self.store = []

    def addVertex(self, val):
        x = vertex(val)
        self.store += [x]

        return len(self.store)
        
    def addEdge(self, a, b, weight):
        self.store[a] 

    def breadthTraversal(self, start):
        C = queue()
        Discovered = []
        Processed = []
        for i in len(self.store):
            Discovered += [False]
            Processed += [False]

        for i in len(self.store):
            if Discovered[i] == False:
                C.enqueue(self.store[i])
                Discovered[i] = True
            while C.length > 0:
                w = C.dequeue()
                if Processed[w[0][0]] == False:
                    print(w[0][0])
                    Processed[w[0][0]] = True
                for vertex in self.store[w]