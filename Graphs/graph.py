from ds import *

class vertex:
    def __init__(self, val):
        self.val = val
        self.edges = []

    def addEdge(self, toVertex, weight):
        self.edges += [[toVertex, weight]]
        return True


class graph:
    def __init__(self):
        self.store = []

    def addVertex(self, val):
        x = vertex(val)
        self.store += [x]

        return len(self.store)
        
    def addEdge(self, a, b, weight):
        self.store[a].addEdge(self.store[b], weight) 

    def breadthTraversal(self, start):

        x = queue()
        x.enqueue(self.store[start])
        visited = []
        while x.length > 0:
            curr = x.dequeue()
            if curr.val in visited:
                continue

            visited += [curr.val]
            for edge in curr.edges:
                x.enqueue(edge[0])

        return visited

    def depthTraversal(self, start):

        x = stack()
        x.push(self.store[start])
        visited = []
        while x.length > 0:
            curr = x.pop()
            if curr.val in visited:
                continue

            visited += [curr.val]
            for edge in curr.edges:
                x.push(edge[0])

        return visited



g = graph()

g.addVertex(0)
g.addVertex(1)
g.addVertex(2)
g.addVertex(3)
g.addVertex(4)


g.addEdge(0, 1, 1)
g.addEdge(0, 2, 1)
g.addEdge(0, 3, 1)

g.addEdge(1, 2, 1)

g.addEdge(2, 3, 1)
g.addEdge(2, 4, 1)

g.addEdge(3, 0, 1)

print(g.breadthTraversal(0))
print(g.depthTraversal(0))


        