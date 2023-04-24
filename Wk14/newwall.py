class Graph:
    def __init__(self,n):
        self.n = n+1
        self.adj_list = {(i,j): set([(i,j)]) for i in range(self.n+1) for j in range(self.n+1)}
        self.graph = {(i, j): {(i, j): 0 for i in range(self.n) for j in range(self.n)} for i in range(self.n) for j in range(self.n)}

    def add_link(self,a,b):
        self.graph[a][b] = 1
        self.adj_list[a].add(b)
        self.adj_list[b].add(a)

    def calculate(self, s, t):
        self.graph_copy = {(i, j): {(k, l): self.graph[(i,j)][(k,l)] for k in range(self.n) for l in range(self.n)} for i in range(self.n) for j in range(self.n)}
        total = 0
        while self.bfs(s, t):
            while True:
                flow = self.dfs(s, t, float('inf'))
                if flow == 0:
                    break
                total += flow
        return total

    def bfs(self, s, t):
        self.level = {(i,j):-1 for i in range(self.n+1) for j in range(self.n+1)}
        self.level[s] = 0
        queue = [s]
        while len(queue) > 0:
            u = queue.pop(0)
            for v in self.adj_list[u]:
                if self.graph_copy[u][v] > 0 and self.level[v] == -1:
                    self.level[v] = self.level[u] + 1
                    queue.append(v)
        return self.level[t] != -1
        
    def dfs(self, x, y, f):
        if x == y:
            return f
        for v in self.adj_list[x]:
            if self.graph_copy[x][v] > 0 and self.level[v] == self.level[x] +1:
                d = self.dfs(v, y, min(f, self.graph_copy[x][v]))
                if d > 0:
                    self.graph_copy[x][v] -= d
                    self.graph_copy[v][x] += d
                    return d
        return 0
    
def count(r):
    g = Graph(len(r))
    for i in range(len(r)):
        for j in range(len(r)):
            if r[i][j] == '.':
                if i < len(r)-1 and r[i+1][j] == '.':
                    g.add_link((i,j),(i+1,j))
                if j < len(r)-1 and r[i][j+1] == '.':
                    g.add_link((i,j), (i,j+1))
    print(g.calculate((0,0), (len(r), len(r))))

    

if __name__ == "__main__":
    r = [".....",
         ".###.",
         "...#.",
         "##.#.",
         "....."]
    print(count(r)) # 2

    r = ["....."
        "....."
        "..#.#"
        "....."
        "..#.."]
    print(count(r))