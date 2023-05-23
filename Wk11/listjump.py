import math
from heapq import heappop, heappush

def calculate(t):
    edges = [[] for _ in range(len(t))]
    for i in range(len(t)):
        if i-t[i] >=0:
            edges[i].append((i-t[i], t[i]))
        if i+t[i] < len(t):
            edges[i].append((i+t[i], t[i]))
    dist = [math.inf]*len(t)
    dist[0] = 0
    v = [False]*len(t)
    heap = []
    heappush(heap, (0, 0))
    while len(heap) > 0:
        item, x = heappop(heap)
        if v[x]:
            continue
        v[x] = True
        for edge in edges[x]:
            if dist[x] + edge[1] < dist[edge[0]]:
                dist[edge[0]] = dist[x] + edge[1]
                heappush(heap, (dist[edge[0]], edge[0]))
    return -1 if dist[-1] == math.inf else dist[-1]

if __name__ == "__main__":
    print(calculate([1,1,1,1])) # 3
    print(calculate([3,2,1])) # -1
    print(calculate([3,5,2,2,2,3,5])) # 10
    print(calculate([7,5,3,1,4,2,4,6,1])) # 32

# Annettuna on lista, jossa on n alkiota. Jokainen alkio on kokonaisluku väliltä 1…n.

# Lähdet liikkelle listan alusta, ja aina kun olet alkion x kohdalla, saat hypätä x
# askelta vasemmalle tai oikealle. Et saa kuitenkaan tehdä hyppyä, joka veisi listan ulkopuolelle. 
# Tavoitteesi on päästä listan loppuun niin, että hyppyjen kokonaismatka on mahdollisimman pieni.

# Esimerkiksi listassa [3,5,2,2,2,3,5] paras ratkaisu on hypätä ensin 3 askelta oikealle, 
# sitten 2 askelta vasemmalle ja lopuksi 5 askelta oikealle. Tässä askelia on yhteensä 3+2+5=10.

# Voit olettaa, että n on enintään 10**5. Jos mitään ratkaisua ei ole olemassa, palauta −1.

# Toteuta tiedostoon listjump.py funktio calculate, joka antaa pienimmän kokonaismatkan.