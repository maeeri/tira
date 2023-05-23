from heapq import heappop, heappush
import math

class AllRoutes:
    def __init__(self,n):
        self.n = n
        self.distances = [[-1]*(n) for _ in range(n)]
        self.roads = [[] for _ in range(n+1)]
        for i in range(n):
            for j in range(n):
                if i==j:
                    self.distances[i][j] = 0


    def add_road(self,a,b,x):
        self.distances[a-1][b-1] = x
        self.distances[b-1][a-1] = x
        self.roads[a].append((b, x))
        self.roads[b].append((a, x))

    def get_table(self):
        visited = {(i, j): False for i in range(self.n+1) for j in range(self.n+1) if i < j}
        for i in range(self.n+1):
            for j in range(self.n+1):
                if i<j and not visited[(i,j)]:
                    x = self.find_route(i,j)
                    if x < self.distances[i-1][j-1] or self.distances[i-1][j-1] == -1 and x < math.inf:
                        self.distances[i-1][j-1] = x
                        self.distances[j-1][i-1] = x
        return self.distances
    
    def find_route(self,a,b):
        heap = []
        visited = [False]*(self.n+1)
        distances = [math.inf]*(self.n+1)
        distances[a] = 0
        heappush(heap, (0, a))
        while len(heap) > 0:
            d, x = heappop(heap)
            if visited[x]:
                continue
            visited[x] = True
            for road in self.roads[x]:
                if distances[x] + road[1] < distances[road[0]]:
                    distances[road[0]] = distances[x] + road[1]
                    heappush(heap, (distances[road[0]], road[0]))
        return distances[b]

if __name__ == "__main__":
    a = AllRoutes(4)
    a.add_road(1,2,2)
    a.add_road(1,3,5)
    a.add_road(2,3,1)
    print(a.get_table())
    # [[0,2,3,-1],[2,0,1,-1],[3,1,0,-1],[-1,-1,-1,0]]


# Bittimaassa on n kaupunkia, joiden välillä ei ole vielä teitä. Tehtäväsi on toteuttaa luokka, 
# jonka avulla pystyy lisäämään tien kahden kaupungin välille sekä muodostamaan taulukon kaupunkien 
# välimatkoista.

# Välimatkataulukko on n×n kokoinen taulukko, jonka rivillä a sarakkeessa b lukee lyhin reitin 
# pituus kaupunkien a ja b välillä. Jos mitään reittiä ei ole olemassa, reitin pituus on −1.

# Tässäkin tehtävässä kaikki tiet ovat kaksisuuntaisia eli ei ole väliä, kummin päin kaupungit annetaan. 
# Huomaa, että kahden kaupungin välillä voi olla useita teitä.

# Voit olettaa, että kaupunkeja on enintään 50 ja luokan metodeita kutsutaan enintään 100
# kertaa. Jokaisen tien pituus on kokonaisluku välillä 1…1000.

# Toteuta tiedostoon allroutes.py luokka AllRoutes, jossa on seuraavat metodit:
# - konstruktori, jolle annetaan kaupunkien määrä
# - add_road lisää kaupunkien a ja b välille tien, jonka pituus on x
# - get_table palauttaa välimatkataulukon kaksiulotteisena listana