class UnionFind:
    def __init__(self, size):
        self.parents = [x for x in range(0, size)]
        self.sizes = [0] * size

    def union(self, a, b):
        # joins a and b and puts them in the same subset if they aren't already in the same subset
        p1 = self.find(a)
        p2 = self.find(b)
        size_p1, size_p2 = self.sizes[p1], self.sizes[p2]
        if p1 != p2:
            if size_p1 >= size_p2:
                self.parents[p2] = p1
                self.sizes[p1] += size_p2
            else:
                self.parents[p1] = p2
                self.sizes[p2] += size_p1
        return [size_p1, size_p2, size_p1 + size_p2]

    def find(self, a):
        # finds the topmost parent of a and compresses the path from a to root
        p = a
        while p != self.parents[p]:
            p = self.parents[p]
        root = p
        p = a
        while p != root:
            p, self.parents[p] = self.parents[p], root
        return root

    def setBit(self, a):
        # find a and sets its size to 1. Used to set initial bits to 1.
        p = self.find(a)
        self.sizes[p] = 1

    def getSize(self, a):
        # find the topmost parent of a and returns the size of its full subtree
        p = self.find(a)
        return self.sizes[p]
