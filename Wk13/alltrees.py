# ei toimi vielä
class Knot:
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

class AllTrees:
    def __init__(self,n):
        self.n = n
        self.edges = []
        pass

    def add_edge(self,a,b):
        self.edges.append((a,b))
        pass

    def count(self):
        trees = set()
        for i in range(len(self.edges)):
            knots = {x: Knot(x) for x in range(1, self.n+1)}
            tree = []
            found = set()
            edges = self.edges[i:] + self.edges[:i]
            for a, b in edges:
                if knots[a].union(knots[b]):
                    tree.append((a, b))
                    found.add(a)
                    found.add(b)
            if len(found) == self.n:
                trees.add(tuple(sorted(tree)))
        print(trees)
        return len(trees)

if __name__ == "__main__":
    # a = AllTrees(3)
    # a.add_edge(1,2)
    # print(a.count()) # 0
    # a.add_edge(1,3)
    # print(a.count()) # 1
    # a.add_edge(2,3)
    # print(a.count()) # 3

    a = AllTrees(4)
    a.add_edge(3,4)
    print(a.count())
    a.add_edge(2,4)
    print(a.count())
    a.add_edge(1,3)
    print(a.count())
    a.add_edge(1,4)
    print(a.count())
    a.add_edge(2,3)
    print(a.count())

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