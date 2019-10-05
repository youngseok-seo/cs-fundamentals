class queue:
    def __init__(self):
        self.l = []
        self.length = 0

    def enqueue(self, x):
        self.l += [x]
        self.length += 1

    def dequeue(self):
        y = self.l[0]
        self.l = self.l[1:]
        self.length -= 1
        return y
        
class stack:
    def __init__(self):
        self.l = []
        self.length = 0

    def push(self, x):
        self.l += [x]
        self.length += 1
        return True

    def pop(self):
        y = self.l[-1]
        self.l = self.l[:-1]
        self.length -= 1
        return y

        





    