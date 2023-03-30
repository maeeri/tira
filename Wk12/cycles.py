class Cycles:
    def __init__(self,n):
        self.n = n
        self.graph = [[] for _ in range(n+1)]

    def add_edge(self,a,b):
        self.graph[a].append(b)

    def check(self):
        for i in range(len(self.graph)):
            for j in range(len(self.graph[i])):
                if i == self.graph[i][j]:
                    return True
        visited = [False]*(self.n+1)
        l = []
        for i in range(len(self.graph)):
            self.dfs(i, visited, l)
        visited = [False]*(self.n+1)
        for i in l:
            l2 = []
            self.dfs(i, visited, l2)
            if len(l2) > 1:
                return True
        return False

    def dfs(self, x, visited, l):
        if visited[x]:
            return
        visited[x] = True
        for y in self.graph[x]:
            self.dfs(y, visited, l)
        l.append(x)


if __name__ == "__main__":
    c = Cycles(4)
    c.add_edge(1,2)
    c.add_edge(2,3)
    c.add_edge(1,3)
    c.add_edge(3,4)
    print(c.check()) # False
    c.add_edge(4,2)
    print(c.check()) # True


    c = Cycles(5)
    print(c.check()) # False
    c.add_edge(3,4)
    c.add_edge(4,3)
    c.add_edge(4,1)
    print(c.check()) # True
    c.add_edge(3,1)
    c.add_edge(4,2)
    c.add_edge(2,1)
    c.add_edge(5,5)
    c.add_edge(4,5)