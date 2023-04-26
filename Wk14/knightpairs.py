class Chess:
    def __init__(self) -> None:
        self.blacks = []
        self.knights = []
        self.graph = {(i,j): {(i,j): 0 for i in range(-1,10) for j in range(-1,10)} for i in range(-1,10) for j in range(-1,10)}
        self.adj = {(i,j): set() for i in range(-1,10) for j in range(-1,10)}

        change = True
        for i in range(9):
            change = not change
            for j in range(9):
                if change and j%2==1 or not change and j%2==0:
                    self.blacks.append((i,j))

    def tile_is_black(self, tile):
        return tile in self.blacks
    
    def add_edge(self,a,b):
        self.graph[a][b] = 1
        self.adj[a].add(b)
        self.adj[b].add(a)

    def match(self, s,t):
        for k1 in self.knights:
            for k2 in self.knights:
                x = abs(k1[0]-k2[0])
                y = abs(k1[1]-k2[1])
                if self.tile_is_black(k1) and not self.tile_is_black(k2) and (x==1 and y==2 or x==2 and y==1):
                    self.add_edge((-1,-1), k1)
                    self.add_edge(k1,k2)
                    self.add_edge(k2, (9,9))
        total = 0
        while self.bfs(s, t):
            while True:
                flow = self.dfs(s, t, float('inf'))
                if flow == 0:
                    break
                total += flow
        return total

    def bfs(self, s, t):
        self.level = {(i,j): -1 for i in range(-1,10) for j in range(-1,10)}
        self.level[s] = 0
        queue = [s]
        while queue:
            u = queue.pop(0)
            for v in self.adj[u]:
                if self.graph[u][v] > 0 and self.level[v] == -1:
                    self.level[v] = self.level[u] + 1
                    queue.append(v)
        return self.level[t] != -1
        
    def dfs(self, x, y, f):
        if x == y:
            return f
        for v in self.adj[x]:
            if self.graph[x][v] > 0 and self.level[v] == self.level[x] +1:
                d = self.dfs(v, y, min(f, self.graph[x][v]))
                if d > 0:
                    self.graph[x][v] -= d
                    self.graph[v][x] += d
                    return d
        return 0


def count(r):
    cb = Chess()
    for i in range(len(r)):
        for j in range(len(r[0])):
            if r[i][j] == '.':
                continue
            cb.knights.append((i,j))
    return cb.match((-1,-1),(9,9))

if __name__ == "__main__":
    r = ["*.......",
         "..*...*.",
         "........",
         ".*......",
         "...*....",
         ".......*",
         "........",
         "......*."]
    print(count(r)) # 3

    r = ['.***.*..',
         '..*....*',
         '.*.....*',
         '.*...*..',
         '*......*',
         '........',
         '.....*.*',
         '**.**...']
    print(count(r)) # 5