class Download:
    def __init__(self,n):
        self.n = n+1
        self.adj = [[] for _ in range(self.n)]
        self.graph = {i: {j: 0 for j in range(self.n)} for i in range(self.n)}

    def add_link(self,a,b,x):
        self.graph[a][b] += x
        self.adj[a].append(b)
        self.adj[b].append(a)

    def calculate(self, a, b):
        self.graph_copy = {i: {j: self.graph[i][j] for j in range(self.n)} for i in range(self.n)}
        return self.dinic(a, b)

    def bfs(self, s, t):
        self.level = [-1]*self.n
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

if __name__ == "__main__":
    d = Download(4)
    print(d.calculate(1,4)) # 0
    d.add_link(1,2,5)
    d.add_link(2,4,6)
    d.add_link(1,4,2)
    print(d.calculate(1,4)) # 7
    d.add_link(1,3,4)
    d.add_link(3,2,2)
    print(d.calculate(1,4)) # 8

    #https://www.geeksforgeeks.org/dinics-algorithm-maximum-flow/