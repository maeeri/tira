class Coloring:
    def __init__(self,n):
        self.n = n
        self.edges = [[] for _ in range(self.n+1)]

    def add_edge(self,a,b):
        self.edges[a].append(b)
        self.edges[b].append(a)

    def check(self):
        self.visited = [False]*(self.n+1)
        self.colours = {i: False for i in range(1, self.n+1)}
        for i in range(self.n+1):
            if not self.visited[i]:
                b = self.dfs(i, 1)
            if not b:
                return b
        return b
        

    def dfs(self, x, c):
        if not self.visited[x]:
            self.colours[x] = 1-c
            self.visited[x] = True
            for k in self.edges[x]:
                if not self.dfs(k, self.colours[x]):
                    return False
        if self.visited[x] and c != self.colours[x]:
            return True
        if self.colours[x] == c:
            return False
        return True

if __name__ == "__main__":
    c = Coloring(4)
    c.add_edge(1,2)
    c.add_edge(2,3)
    c.add_edge(3,4)
    c.add_edge(1,4)
    print(c.check()) # True
    c.add_edge(2,4)
    print(c.check()) # False

    c = Coloring(5)
    print(c.check())
    print(c.check())
    c.add_edge(3,4)
    c.add_edge(4,5)
    c.add_edge(4,5)
    print(c.check())
    c.add_edge(4,5)
    c.add_edge(3,5)
    print(c.check())
    print(c.check())