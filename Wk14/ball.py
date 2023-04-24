class Graph:
    def __init__(self,n):
        self.n = n+1
        self.adj = [[] for _ in range(self.n+1)]
        self.graph = {i: {j: 0 for j in range(self.n+1)} for i in range(self.n+1)}

    def add_link(self,a,b):
        self.graph[a][b] = 1
        self.adj[a].append(b)
        self.adj[b].append(a)

    def calculate(self, s, t):
        self.graph_copy = {i: {j: self.graph[i][j] for j in range(self.n+1)} for i in range(self.n+1)}
        total = 0
        while self.bfs(s, t):
            while True:
                flow = self.dfs(s, t, float('inf'))
                if flow == 0:
                    break
                total += flow
        return total

    def bfs(self, s, t):
        self.level = [-1]*(self.n+1)
        self.level[s] = 0
        queue = [s]
        while len(queue) > 0:
            u = queue.pop(0)
            for v in self.adj[u]:
                if self.graph_copy[u][v] > 0 and self.level[v] == -1:
                    self.level[v] = self.level[u] + 1
                    queue.append(v)
        return self.level[t] != -1
        
    def dfs(self, x, y, f):
        if x == y:
            return f
        for v in self.adj[x]:
            if self.graph_copy[x][v] > 0 and self.level[v] == self.level[x] +1:
                d = self.dfs(v, y, min(f, self.graph_copy[x][v]))
                if d > 0:
                    self.graph_copy[x][v] -= d
                    self.graph_copy[v][x] += d
                    return d
        return 0
    
    def dinic(self, s, t):
        total = 0
        while self.bfs(s, t):
            while True:
                flow = self.dfs(s, t, float('inf'))
                if flow == 0:
                    break
                total += flow
        return total

class Ball():
    def __init__(self,n):
        self.n = n
        self.g = Graph(n*2)

    def add_pair(self, a, b):
        b += self.n
        self.g.add_link(a, b)
        self.g.add_link(0, a)
        self.g.add_link(b, self.g.n)
    
    def calculate(self):
        return self.g.calculate(0,self.g.n)
        

 
if __name__ == "__main__":
    b = Ball(4)
    print(b.calculate()) # 0
    b.add_pair(1,2)
    print(b.calculate()) # 1
    b.add_pair(1,3)
    b.add_pair(3,2)
    print(b.calculate()) # 2
