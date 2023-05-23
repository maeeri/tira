# ei toimi vielä
from collections import defaultdict
class Graph:
    def __init__(self,n):
        global inf
        inf = float('inf')
        self.size = n
        self.flow = {(i,j): 0 for i in range(self.size) for j in range(self.size)}
        self.adj_dict = {(i,j): set() for i in range(self.size) for j in range(self.size)}
        self.graph = defaultdict(list)
        self.matrix = {(i, j): {(i, j): 0 for i in range(self.size) for j in range(self.size)} for i in range(self.size) for j in range(self.size)}

    def add_link(self,a,b):
        self.graph[a].append(b)
        self.flow[a] = 1
        self.flow[b] = 1
        self.adj_dict[a].add(b)

    def calculate(self, s, t):
        self.flow[(0,0)] = 2
        self.flow[(self.size-1, self.size-1)] = inf
        self.flow_copy = {(i,j): self.flow[(i,j)] for i in range(self.size) for j in range(self.size)}
        total = 0
        self.paths = set()
        self.dfs(s,t)
        for path in self.paths:
            print(path)
        # while self.bfs(s, t):
        #     while True:
        #         flow = self.dfs(s, t, inf)
        #         if flow == 0:
        #             break
        #         total += flow
        return total

    def bfs(self, s, t):
        self.level = {(i,j):-1 for i in range(self.size+1) for j in range(self.size+1)}
        self.level[s] = 0
        queue = [s]
        while queue:
            u = queue.pop(0)
            for v in self.adj_dict[u]:
                if self.flow[v] > 0 and self.level[v] == -1:
                    self.level[v] = self.level[u] + 1
                    queue.append(v)
        return self.level[t] != -1
        
    def dfs(self, start, end, visited=None, path=None):
        if visited is None:
            visited = set()
        if path is None:
            path = start
        if start == end:
            return path
        for neighbor in self.adj_dict[start]:
            if neighbor not in visited:
                new_path = path, (neighbor)
                self.paths.add((self.dfs(neighbor, end, visited.copy(), new_path)))
        return 
    
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
    # r = [".....",
    #      ".###.",
    #      "...#.",
    #      "##.#.",
    #      "....."]
    # print(count(r)) # 2

    # r = ["...#.",
    #      ".....",
    #      "#....",
    #      "#....",
    #      "#...."]
    # print(count(r))#2

    r = [".....",
         ".....",
         "..#.#",
         ".....",
         "..#.."]
    print(count(r))#1

# Annettuna on n×n -ruudukko, jossa jokainen ruutu on lattiaa tai seinää. Vasemman yläkulman ja oikean 
# alakulman ruudut ovat aina lattiaa eikä niitä voi muuttaa.

# Ruudukossa voi liikkua vain oikealle ja alaspäin. Montako ruutua pitää muuttaa vähintään seinäksi, 
# jotta ruudukossa ei ole mitään reittiä vasemmasta yläkulmasta oikeaan alakulmaan?

# Ruudukon kuvauksessa merkki . tarkoittaa lattiaa ja merkki # tarkoittaa seinää. Voit olettaa, 
# että 1≤n≤20.

# Toteuta tiedostoon newwall.py funktio count, joka antaa pienimmän muutettavien ruutujen määrän.