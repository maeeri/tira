class WallGrid:
    def __init__(self,n):
        self.n = n
        self.grid = [[1]*(n+1) for _ in range(n+1)]
        self.neighbors = {(i,j): [(i-1,j), (i+1,j), (i,j-1), (i,j+1)] for i in range(1, n+1) for j in range(1, n+1)}
        self.link = {(i, j): (i, j) for i in range(self.n+1) for j in range(self.n+1)}
        self.roots = set()
        self.sizes = {(i, j): 0 for i in range(self.n+1) for j in range(self.n+1)}

    def remove(self,x,y):
        if self.grid[x][y] == 0: return

        self.grid[x][y] = 0
        self.sizes[(x, y)] += 1

        temp_roots = [self.find(n) for n in self.neighbors[(x,y)] if self.grid[n[0]][n[1]] == 0 and self.find(n) != self.find((x, y))]
        a = self.find((x, y))

        for z in temp_roots:
            z = self.find(z)
            a = self.find(a)
            self.union(a, z)

        self.roots.add(self.find(a))

    def count(self):
        return len(self.roots)

    def find(self, x):
        while self.link[x] != x:
            x = self.link[x]
        return x
    
    def union(self, a, b):
        if self.sizes[a] < self.sizes[b]:
            a, b = b, a
        self.sizes[a] += self.sizes[b]
        self.link[b] = a
        self.roots.discard(b)
        self.roots.add(a)

if __name__ == "__main__":
    w = WallGrid(6)
    print(w.count())
    print(w.count())
    print(w.count())
    print(w.count())
    print(w.count())
    w.remove(5,4)
    print(w.count())
    print(w.count())
    w.remove(5,4)
    w.remove(2,2)
    w.remove(5,2)
    w.remove(3,3)
    print(w.count())
    print(w.count())
    w.remove(5,3)
    w.remove(4,3)
    print(w.count())
    print(w.count())
    print(w.count())
    w.remove(2,3)
    w.remove(3,4)
    print(w.count())
    print(w.count())
    print(w.count())
    w.remove(4,3)
    print(w.count())
    print(w.count())
    w.remove(4,3)
    print(w.count())
    print(w.count())

# Ruudukossa on n×n ruutua, joista jokainen on aluksi seinää. Rivit ja sarakkeet on numeroitu 1…n. 
# Ruudukosta aletaan poistaa seinää muuttamalla seinäruutuja lattiaruuduiksi.

# Tehtäväsi on pitää kirjaa huoneiden määrästä tässä prosessissa. Huoneissa lattiaruutuja voi kulkea 
# vaaka- ja pystysuuntaisesti, kuten aiemmissa kurssin tehtävissä.

# Voit olettaa, että n on enintään 100 ja luokan metodeita kutsutaan enintään 10000 kertaa. 
# Lisäksi reunaruutuja ei koskaan muuteta lattiaksi.

# Toteuta tiedostoon wallgrid.py luokka WallGrid, jossa on seuraavat metodit:
# - konstruktori, jolle annetaan ruudukon koko
# - remove muuttaa ruudun (x,y) lattiaksi, mikäli se ei jo ole lattiaa
# - count ilmoittaa, montako huonetta ruudukossa on