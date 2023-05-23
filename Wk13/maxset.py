from time import time
class MaxSet:
    def __init__(self,n):
        self.n = n
        self.links = list(range(self.n+1))
        self.sizes = [1]*(self.n+1)
        self.max = 1

    def merge(self,a,b):
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return
        if self.sizes[a] < self.sizes[b]:
            a, b = b, a
        self.sizes[a] += self.sizes[b]
        self.links[b] = a
        if self.sizes[a] > self.max: self.max = self.sizes[a]

    def get_max(self):
        return self.max

    def find(self, x):
        while self.links[x] != x:
            x = self.links[x]
        return x

if __name__ == "__main__":
    m = MaxSet(5)
    print(m.get_max()) # 1
    m.merge(1,2)
    m.merge(3,4)
    m.merge(3,5)
    print(m.get_max()) # 3
    m.merge(1,5)
    print(m.get_max()) # 5

# Luvut 1,2,…,n ovat aluksi jokainen omassa joukossaan. Tehtäväsi on toteuttaa luokka, jossa voi yhdistää 
# kaksi joukkoa sekä hakea suurimman joukon koon.

# Voit olettaa, että n on enintään 105 ja luokan metodeita kutsutaan enintään 105 kertaa.

# Toteuta tiedostoon maxset.py luokka MaxSet, jossa on seuraavat metodit:
# - konstruktori, jolle annetaan lukujen määrä
# - merge yhdistää joukot, joissa on luvut a ja b (jos ne ovat eri joukoissa)
# - get_max ilmoittaa suurimman joukon koon