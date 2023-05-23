from collections import deque

class Network:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.graph = {(n,m): [] for n in range(self.n+1) for m in range(self.m+1)}

    def add_link(self, a, b):
        self.graph[a].append(b)
        self.graph[b].append(a)

    def best_route(self, a, b):
        self.q = deque()
        self.visited = {(n,m): False for n in range(self.n+1) for m in range(self.m+1)}
        self.distances = {(n,m): -1 for n in range(self.n+1) for m in range(self.m+1)}
        self.bfs(a)
        return self.distances[b] if self.distances[b] else -1

    def bfs(self, x):
        self.q.append(x)
        self.visited[x] = True
        self.distances[x] = 0
        while len(self.q)>0:
            knot = self.q.popleft()
            for y in self.graph[knot]:
                if self.visited[y]:
                    continue
                self.q.append(y)
                self.visited[y] = True
                self.distances[y] = self.distances[knot]+1

def count(r):
    network = Network(len(r), len(r[0]))
    floor = ['A', 'B', '.']
    a, b = (0,0), (0,0)
    for i in range(1, len(r)):
        for j in range(1, len(r[i])):
            if r[i][j] in floor:
                if r[i][j-1] in floor:
                    network.add_link((i,j), (i,j-1))
                if r[i-1][j] in floor:
                    network.add_link((i,j), (i-1,j))
            if r[i][j] == 'A':
                a = (i,j)
            if r[i][j] == 'B':
                b = (i,j)
    return network.best_route(a,b)

if __name__ == "__main__":
    r = ["########",
         "#.A....#",
         "#.#.##.#",
         "####.#.#",
         "#...B#.#",
         "########"]
    print(count(r)) # 7

# Annettuna on n×m -ruudukko, joka esittää labyrinttiä. Tehtäväsi on laskea lyhimmän reitin pituus 
# ruudusta A ruutuun B. Jokainen ruutu on joko lattiaa (.) tai seinää 
# (#), ja jokainen reunalla oleva ruutu on seinää.

# Voit olettaa, että 1≤n,m≤20. Jos mitään reittiä ei ole olemassa, palauta −1.

# Toteuta tiedostoon labyrinth.py funktio count, joka kertoo lyhimmän reitin pituuden.