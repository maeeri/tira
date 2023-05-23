def count(r):
    global matrix, walls, visited
    matrix = []
    walls = []
    visited = []
    counter = 0
    for i in range(len(r)):
        temp = []
        visited.append([])
        visited[i] = []
        for j in range(len(r[i])):
            temp.append(r[i][j])
            visited[i].append(False)
            if r[i][j] == '#':
                walls.append((i,j))
        matrix.append(temp)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if (i, j) not in walls and not visited[i][j]: 
                dfs(i, j, len(matrix), len(matrix[i]))
                counter += 1

    return counter


def dfs(y, x, n, m):
    global matrix, walls, visited
    if y < 0 or x < 0 or y >= n or x >= m:
        return
    if (y, x) in walls or visited[y][x]:
        return
    visited[y][x] = True
    dfs(y+1, x, n, m)
    dfs(y-1, x, n, m)
    dfs(y, x+1, n, m)
    dfs(y, x-1, n, m)

if __name__ == "__main__":
    r = ["########",
         "#..#...#",
         "####.#.#",
         "#..#.#.#",
         "########"]
    print(count(r)) # 3

# Annettuna on n×m -ruudukko, joka esittää talon pohjapiirrosta. Jokainen ruutu on joko lattiaa (.) 
# tai seinää (#), ja jokainen reunalla oleva ruutu on seinää.

# Kaksi lattiaruutua kuuluvat samaan huoneeseen, jos ne ovat vierekkäin pysty- tai vaakasuunnassa. 
# Montako huonetta talossa on?

# Voit olettaa, että 1≤n,m≤20.

# Toteuta tiedostoon chambers.py funktio count, joka antaa huoneiden määrän.