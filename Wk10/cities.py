class Cities:
    def __init__(self,n):
        self.n = n
        self.connections = [[] for _ in range(self.n+1)]
        
    def add_road(self,a,b):
        self.connections[a].append(b)
        self.connections[b].append(a)

    def has_route(self,a,b):
        self.visited = {}
        for i in range(1, self.n+1):
            self.visited[i] = False
        self.find_routes(a)
        return self.visited[a] and self.visited[b]

    def find_routes(self, x):
        if self.visited[x]:
            return
        self.visited[x] = True
        for x in self.connections[x]:
            self.find_routes(x)

if __name__ == "__main__":
    c = Cities(5)
    c.add_road(1,2)
    c.add_road(1,3)
    c.add_road(4,5)
    print(c.has_route(1,5)) # False
    c.add_road(3,4)
    print(c.has_route(1,5)) # True

# Bittimaassa on n kaupunkia, joiden välillä ei ole vielä teitä. 
# Tehtäväsi on toteuttaa luokka, jonka avulla pystyy lisäämään tien kahden kaupungin 
# välille sekä tutkimaan, onko kahden kaupungin välillä reittiä.

# Voit olettaa, että kaupunkeja on enintään 50 ja luokan metodeita kutsutaan enintään 100 kertaa.

# Toteuta tiedostoon cities.py luokka Cities, jossa on seuraavat metodit:
# - konstruktori, jolle annetaan kaupunkien määrä
# - add_road lisää tien kahden kaupungin välille
# - has_route tarkastaa, onko kahden kaupungin välillä reittiä