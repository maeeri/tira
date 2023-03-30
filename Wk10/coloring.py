class Coloring:
    def __init__(self,n):
        self.n = n
        self.edges = [[] for _ in range(self.n)]

    def add_edge(self,a,b):
        self.edges[a].append(b)
        self.edges[b].append(a)

    def check(self):
        pass

if __name__ == "__main__":
    c = Coloring(4)
    c.add_edge(1,2)
    c.add_edge(2,3)
    c.add_edge(3,4)
    c.add_edge(1,4)
    print(c.check()) # True
    c.add_edge(2,4)
    print(c.check()) # False