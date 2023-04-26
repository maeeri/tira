class Graph:
    def __init__(self,n):
        global inf
        inf = float('inf')
        self.paths = []
        self.size = n
        self.adj_dict = {(i,j): set() for i in range(self.size) for j in range(self.size)}
        self.matrix = {(i, j): {(i, j): inf for i in range(self.size) for j in range(self.size)} for i in range(self.size) for j in range(self.size)}

    def add_link(self,a,b):
        self.matrix[a][b] = 1
        self.adj_dict[a].add(b)

    def calculate(self, s, t):
        for x in self.adj_dict[s]:
            self.visited = {(i,j): False for i in range(self.size+1) for j in range(self.size+1)}
            self.dfs(x, t, [x])
        r = []
        for k in self.adj_dict:
            counter = 0
            for path in self.paths:
                if k in path:
                    counter += 1
            if counter > 0: r.append(counter)
        return r
        
    def dfs(self, x, y, temp):
        if x == y:
            temp.pop()
            self.paths.append(temp)
            return
        self.visited[x] = True
        for v in self.adj_dict[x]:
            if not self.visited[v]:
                self.dfs(v, y, temp + [v])
        

def count(r):
    g = Graph(len(r))
    for i in range(len(r)):
        for j in range(len(r[0])):
            if r[i][j] == '.':
                if i < len(r)-1 and r[i+1][j] == '.':
                    g.add_link((i,j),(i+1,j))
                if j < len(r)-1 and r[i][j+1] == '.':
                    g.add_link((i,j), (i,j+1))
    return g.calculate((0,0), (len(r)-1, len(r)-1))

    

if __name__ == "__main__":
    r = [".....",
         ".###.",
         "...#.",
         "##.#.",
         "....."]
    print(count(r)) # 2

    r = ["...#.",
         ".....",
         "#....",
         "#....",
         "#...."]
    print(count(r)) #2

    r = [".....",
         ".....",
         "..#.#",
         ".....",
         "..#.."]
    print(count(r))#1