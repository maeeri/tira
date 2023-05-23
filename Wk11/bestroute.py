from heapq import heappop, heappush
import math

class BestRoute:
    def __init__(self,n):
        self.n = n
        self.roads = [[] for i in range(n+1)]

    def add_road(self,a,b,x):
        self.roads[a].append((b, x))
        self.roads[b].append((a, x))
           
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
                if  distances[x] + road[1] < distances[road[0]]:
                    distances[road[0]] = distances[x] + road[1]
                    heappush(heap, (distances[road[0]], road[0]))
        return -1 if distances[b] == math.inf else distances[b]

        

if __name__ == "__main__":
    b = BestRoute(3)
    b.add_road(1,2,2)
    print(b.find_route(1,3)) # -1
    b.add_road(1,3,5)
    print(b.find_route(1,3)) # 5
    b.add_road(2,3,1)
    print(b.find_route(1,3)) # 3

    b = BestRoute(5)
    b.add_road(4,5,9)
    b.add_road(1,2,10)
    print(b.find_route(4,5))
    b.add_road(2,4,5)
    b.add_road(3,5,4)
    print(b.find_route(1,3))
    print(b.find_route(2,5))
    b.add_road(3,5,9)
    b.add_road(2,4,1)
    b.add_road(4,5,1)

# Bittimaassa on n kaupunkia, joiden välillä ei ole vielä teitä. Tehtäväsi on toteuttaa luokka, 
# jonka avulla pystyy lisäämään tien kahden kaupungin välille sekä etsimään lyhimmän reitin kahden 
# kaupungin välillä.

# Huomaa, että kaikki tiet ovat kaksisuuntaisia eli ei ole väliä, kummin päin kaupungit annetaan.

# Voit olettaa, että kaupunkeja on enintään 50 ja luokan metodeita kutsutaan enintään 100 kertaa. 
# Jokaisen tien pituus on kokonaisluku välillä 1…1000.

# Toteuta tiedostoon bestroute.py luokka BestRoute, jossa on seuraavat metodit:
# - konstruktori, jolle annetaan kaupunkien määrä
# - add_road lisää kaupunkien a ja b välille tien, jonka pituus on x
# - find_route ilmoittaa lyhimmän reitin pituuden kaupunkien a ja b välillä 
#   (tai −1, jos mitään reittiä ei ole)