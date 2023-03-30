
class GraphGame:
    def __init__(self,n):
        self.n = n
        self.graph = [[] for _ in range(self.n+1)]
        self.paths = {i: [] for i in range(1, self.n +1)}
        self.change = False

    def add_link(self,a,b):
        self.graph[a].append(b)
        self.change = True

    def dfs(self, x, l, visited):
        if visited[x]:
            return
        visited[x] = True
        for y in self.graph[x]:
            self.dfs(y, l, visited)
        l.append(x)

    def get_paths(self):
        for x in range(1, self.n+1):
            l = []
            visited = [False]*(len(self.graph)+1)
            self.dfs(x, l, visited)
            l.reverse()
            print(l)
            if len(l) > 1 and tuple(l[1:]) not in self.paths[l[0]]: self.paths[l[0]].append(tuple(l[1:]))
        self.change = False

    def winning(self,x):
        if self.change:
            self.get_paths()
        if len(self.paths[x]) == 0: return False
        print(self.paths[x])
        for path in self.paths[x]:
            print(x, path)


if __name__ == "__main__":
    g = GraphGame(6)
    g.add_link(3,4)
    g.add_link(1,4)
    g.add_link(4,5)
    print(g.winning(3)) # False
    print(g.winning(1)) # False
    g.add_link(3,1)
    g.add_link(4,6)
    g.add_link(6,5)
    print(g.winning(3)) # True
    print(g.winning(1)) # False
    print(g.winning(2)) # False