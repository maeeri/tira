class LongPath:
    def __init__(self,n):
        self.n = n
        self.graph = [[] for _ in range(n+1)]
        self.paths = []

    def add_edge(self,a,b):
        self.graph[a].append(b)
        self.graph[b].append(a)
        self.graph[a].sort()
        self.graph[b].sort()

    def calculate(self):
        visited = [False] * (self.n+1)
        r = []
        for i in range(len(self.graph)):
            l = self.dfs(i, visited, [])
            r.append(l)
            print(l)
            print('paths:', self.paths)
        return max(r)

    def dfs(self, x, visited, l):
        r = []
        if visited[x]:
            return l
        visited[x] = True
        if len(l) > 0 and x <= l[-1]:    
            return l
        else:
            l.append(x)
            for y in self.graph[x]:
                self.paths.append(self.dfs(y, visited, l))
        return l
        
        

if __name__ == "__main__":
    # l = LongPath(4)
    # l.add_edge(1,2)
    # l.add_edge(1,3)
    # l.add_edge(2,4)
    # l.add_edge(3,4)
    # print(l.calculate()) # 2
    # l.add_edge(3,2)
    # print(l.calculate()) # 3

    l = LongPath(5)
    print(l.calculate()) # 0
    l.add_edge(3,5)
    print(l.calculate()) # 1
    print(l.calculate()) # 1
    l.add_edge(3,4)
    print(l.calculate()) # 1
    l.add_edge(5,4)
    l.add_edge(1,2)
    l.add_edge(3,1)
    print(l.calculate()) # 4