class Knot:
    def __init__(self, val) -> None:
        self.val = val
        self.group = self
        self.group_size = 1
    
    def find(self):
        if self.group != self:
            self.group = self.group.find()
        return self.group
    
    def union(self, other):
        rep1 = self.find()
        rep2 = other.find()
        if rep1 == rep2:
            return False
        if rep1.group_size > rep2.group_size:
            rep2.group = rep1
            rep1.group_size += rep2.group_size
            rep2.group_size = rep1.group_size
        else:
            rep1.group = rep2
            rep2.group_size += rep1.group_size
            rep1.group_size = rep2.group_size
        return True

class SameWeight:
    def __init__(self,n):
        self.n = n
        self.edges = []

    def add_edge(self,a,b,x):
        self.edges.append((x, a, b))

    def check(self):
        self.knots = {i: Knot(i) for i in range(1, self.n+1)}
        smallest = 0
        for w, a, b in sorted(self.edges):
            if self.knots[a].union(self.knots[b]):
                smallest += w
        self.knots = {i: Knot(i) for i in range(1, self.n+1)}
        largest = 0
        for w, a, b in sorted(self.edges, reverse=True):
            if self.knots[a].union(self.knots[b]):
                largest += w
        u = True
        for x in self.knots:
            if self.knots[x].group_size == self.n:
                u = False
                break
        return smallest == largest or u

if __name__ == "__main__":
    s = SameWeight(4)
    s.add_edge(1,2,2)
    s.add_edge(1,3,3)
    print(s.check()) # True
    s.add_edge(1,4,3)
    print(s.check()) # True
    s.add_edge(3,4,3)
    print(s.check()) # True
    s.add_edge(2,4,1)
    print(s.check()) # False

    s = SameWeight(5)
    s.add_edge(2,5,1)
    s.add_edge(3,4,10)
    s.add_edge(4,5,9)
    s.add_edge(3,5,5)
    print(s.check()) # True
    print(s.check()) # True
    s.add_edge(2,4,1)
    print(s.check())
    print(s.check())