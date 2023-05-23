from heapq import heappush, heappop

def count(r):
    n = len(r)
    m = len(r[0])
    start = ()
    end = ()
    graph = {(i,j): {(k,l): float('inf') for k in range(n) for l in range(m)} for i in range(n) for j in range(m)}
    for i in range(n):
        for j in range(m):
            tile = r[i][j]
            if tile == '#': continue
            if tile == 'A': start = (i,j)
            if tile == 'B': end = (i,j)
            if 1 < i:
                graph[(i,j)][(i-1,j)] = 1 if r[i-1][j] == '*' else 0
            if 1 < j:
                graph[(i,j)][(i,j-1)] = 1 if r[i][j-1] == '*' else 0
            if i < n-1:
                graph[(i,j)][(i+1,j)] = 1 if r[i+1][j] == '*' else 0            
            if j < m-1:
                graph[(i,j)][(i,j+1)] = 1 if r[i][j+1] == '*' else 0
    
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = [(0, start)]

    while queue:
        (dist, current) = heappop(queue)

        for neighbor, weight in graph[current].items():
            distance = distances[current] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heappush(queue, (distance, neighbor))
    
    return distances[end]

if __name__ == "__main__":
    r = ["########",
         "#*A*...#",
         "#.*****#",
         "#.**.**#",
         "#.*****#",
         "#..*.B.#",
         "########"]
    print(count(r)) # 2

# Annettuna on n×m -labyrintti, ja tehtäväsi on kulkea ruudusta A ruutuun B.

# Tässä tehtävässä labyrintissa on kahdenlaisia seinäruutuja: labyrintin reunalla olevaa seinää 
# merkitään # kuten ennenkin, mutta labyrintin sisällä olevaa seinää merkitään *. 
# Voit rikkoa labyrintin sisällä olevaa seinää, jolloin pystyt kulkemaan vapaammin labyrintissa.

# Mikä on pienin mahdollinen määrä seinäruutuja, jotka sinun täytyy rikkoa, jotta pääset maaliin? 
# Voit olettaa, että 1≤n,m≤20.

# Toteuta tiedostoon breakwall.py funktio count, joka kertoo pienimmän 
# mahdollisen määrän rikottavia seinäruutuja.