from collections import deque

class Network:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(self.n+1)]

    def add_link(self, a, b):
        self.graph[a].append(b)
        self.graph[b].append(a)

    def best_route(self, a, b):
        self.q = deque()
        self.visited = [False for _ in range(self.n+1)]
        self.distances = [[] for _ in range(self.n+1)]
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


if __name__ == "__main__":
    w = Network(5)
    w.add_link(1,2)
    w.add_link(2,3)
    w.add_link(1,3)
    w.add_link(4,5)
    print(w.best_route(1,5)) # -1
    w.add_link(3,5)
    print(w.best_route(1,5)) # 2

# Verkossa on n tietokonetta, joiden välillä ei ole vielä yhteyksiä. Tehtäväsi on toteuttaa luokka, 
# jonka avulla pystyy lisäämään yhteyden kahden koneen välille sekä etsimään suorimman reitin kahden 
# koneen välillä.

# Voit olettaa, että tietokoneita on enintään 50 ja luokan metodeita kutsutaan enintään 100 kertaa.

# Toteuta tiedostoon network.py luokka Network, jossa on seuraavat metodit:
# - konstruktori, jolle annetaan tietokoneiden määrä
# - add_link lisää yhteyden kahden koneen välille
# - best_route palauttaa pienimmän yhteyksien määrän reitillä kahden koneen välillä 
#   (tai −1 jos reittiä ei ole)