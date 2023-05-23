class Components:
    def __init__(self,n):
        self.n = n
        self.link = list(range(n+1))
        self.size = [1]*(n+1)

    def add_road(self,a,b):
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return
        if self.size[a] < self.size[b]:
            a, b = b, a
        self.size[a] += self.size[b]
        self.link[b] = a

    def count(self):
        count = 0
        roots = set()
        for l in self.link:
            r = self.find(l)
            if l == 0:
                continue
            if r not in roots:
                count += 1
                roots.add(r)
        return count

    def find(self, x):
        while self.link[x] != x:
            x = self.link[x]
        return x
        

if __name__ == "__main__":
    c = Components(5)
    print(c.count()) # 5
    c.add_road(1,2)
    c.add_road(1,3)
    print(c.count()) # 3
    c.add_road(2,3)
    print(c.count()) # 3
    c.add_road(4,5)
    print(c.count()) # 2

# Bittimaassa on n kaupunkia, joiden välillä ei ole aluksi teitä. Kaksi kaupunkia kuuluvat samaan 
# komponenttiin, jos niiden välillä pystyy kulkemaan teiden avulla.

# Tehtäväsi on toteuttaa luokka, jonka avulla pystyy lisäämään tien kahden kaupungin välille sekä 
# laskemaan, montako komponenttia kaupungit muodostavat.

# Voit olettaa, että kaupunkeja on enintään 50 ja luokan metodeita kutsutaan enintään 100 kertaa.

# Toteuta tiedostoon components.py luokka Components, jossa on seuraavat metodit:
# - konstruktori, jolle annetaan kaupunkien määrä
# - add_road lisää tien kahden kaupungin välille
# - count ilmoittaa komponenttien määrän