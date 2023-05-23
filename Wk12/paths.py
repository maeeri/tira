class Graph:
    def __init__(self, n):
        self.graph = [[] for _ in range(101)]
        self.edges = []

    def add_link(self, a, b):
        self.graph[a].append(b)

    def check(self, x, y):
        pass

def create(x):
    pass

if __name__ == "__main__":
    print(create(2)) # esim. [(1,2),(1,100),(2,100)]
    # print(create(5))
    # print(create(10))
    # print(create(123456789))

# Tehtäväsi on muodostaa syklitön suunnattu verkko, jossa on 100 solmua ja tasan x erilaista polkua 
# solmusta 1 solmuun 100. Verkossa saa olla korkeintaan 1000 kaarta ja jokaisen kaaren tulee olla erilainen.

# Esimerkiksi kun x=5, yksi mahdollinen ratkaisu muodostuu kaarista
# (1,3),(1,5),(2,100),(3,2),(3,100),(5,2),(5,3).

# Tässä tapauksessa polut ovat seuraavat:

# - 1→3→100
# - 1→3→2→100
# - 1→5→2→100
# - 1→5→3→100
# - 1→5→3→2→100

# Voit olettaa, että x on kokonaisluku välillä 1…109. Voit muodostaa minkä tahansa verkon, joka 
# täyttää yllä olevat vaatimukset.

# Toteuta tiedostoon paths.py funktio create, joka palauttaa verkon rakenteen listana kaaria tupleina.