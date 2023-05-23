class Graph:
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

class Planets:
    def __init__(self,n):
        self.n = n
        self.g = Graph(n)
        

    def add_teleport(self,a,b):
        self.g.add_link(a, b, 1)

    def calculate(self):
        return self.g.calculate(1, self.n)

if __name__ == "__main__":
    p = Planets(5)
    print(p.calculate()) # 0
    p.add_teleport(1,2)
    p.add_teleport(2,5)
    print(p.calculate()) # 1
    p.add_teleport(1,5)
    print(p.calculate()) # 2

# Pelissä on n planeettaa, jotka on numeroitu 1,2,…,n. Pelaaja aloittaa planeetalta 1 ja voittaa pelin, 
# kun pääsee planeetalle n.

# Planeettojen välillä voi liikkua teleporteilla. Jokainen teleportti voidaan kuvata parilla (a,b), 
# missä a<b: teleportti vie planeetalta a planeetalle b.

# Olet päässyt pelin läpi itse, mutta haluat estää, että kukaan voi enää voittaa peliä. Montako 
# teleporttia sinun tulee poistaa vähintään pelistä?

# Voit olettaa, että n on enintään 50 ja luokan metodeita kutsutaan enintään 100 kertaa.

# Toteuta tiedostoon planets.py luokka Planets, jossa on seuraavat metodit:
# - konstruktori, jolle annetaan määrä n
# - add_teleport lisää teleportin planeetalta a planeetalle b
# - calculate ilmoittaa pienimmän poistettavien teleporttien määrän