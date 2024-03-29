class City:
    def __init__(self, val) -> None:
        self.val = val
        self.group = self
        self.group_size = 1
    
    def find(self):
        if self.group != self:
            self.group = self.group.find()
        return self.group
    
    def union(self, other):
        rep1 = self.find()
        rep2 = other.find()
        if rep1 == rep2:
            return False
        if rep1.group_size > rep2.group_size:
            rep2.group = rep1
            rep1.group_size += rep2.group_size
            rep2.group_size = rep1.group_size
        else:
            rep1.group = rep2
            rep2.group_size += rep1.group_size
            rep1.group_size = rep2.group_size
        return True

class NewRoads:
    def __init__(self,n):
        self.n = n
        self.roads = []

    def add_road(self,a,b,x):
        self.roads.append((x, a, b))

    def min_cost(self):
        self.cities = {i: City(i) for i in range(1, self.n+1)}
        cost = 0
        for w, a, b in sorted(self.roads):
            if self.cities[a].union(self.cities[b]):
                cost += w
        return cost if self.cities[1].find().group_size == self.n else -1

if __name__ == "__main__":
    n = NewRoads(4)
    n.add_road(1,2,2)
    n.add_road(1,3,5)
    print(n.min_cost()) # -1
    n.add_road(3,4,4)
    print(n.min_cost()) # 11
    n.add_road(2,3,1)
    print(n.min_cost()) # 7

# Bittimaassa on n kaupunkia, joiden välillä ei ole alussa teitä. Tavoitteena on yhdistää kaikki 
# kaupungit toisiinsa teiden avulla.

# Annettuna on joukko mahdollisia teitä ja jokaisesta tiestä rakentamisen hinta. Mikä on pienin kustannus, 
# jolla voidaan rakentaa tieverkosto niin, että jokaisen kahden kaupungin välillä on reitti?

# Voit olettaa, että kaupunkeja on enintään 50 ja luokan metodeita kutsutaan enintään 100 kertaa. 
# Jokaisen tien pituus on kokonaisluku välillä 1…1000.

# Toteuta tiedostoon newroads.py luokka NewRoads, jossa on seuraavat metodit:
# - konstruktori, jolle annetaan kaupunkien määrä
# - add_road tarjoaa kaupunkien a ja b välille tietä, jonka hinta on x
# - min_cost ilmoittaa pienimmän rakentamisen kokonaiskustannuksen 
#   (tai −1, jos ei ole mahdollista yhdistää kaikkia kaupunkeja)