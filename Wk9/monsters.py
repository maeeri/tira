def recursion(r, x=0, y=0, m={}):
    if (x, y) in m:
        return m[(x, y)]
    m[(0,0)] = (0, True)
    for i in range(x, len(r)):
        for j in range(len(r[0])):
            if r[i][j] =='#' or (i>0 and j>0 and r[i][j-1] == '#' and r[i-1][j] == '#'):
                m[(i,j)] = (0, False)
                continue
            a = recursion(r, i-1, j, m) if i > 0 else None
            b = recursion(r, i, j-1, m) if j > 0 else None
            if a and a[1] and b and b[1]:
                m[(i,j)] = (min(a[0], b[0]), True)
            elif a and a[1]:
                m[(i,j)] = a
            elif b and b[1]:
                m[(i,j)] = b
            elif i>0 or j>0:
                m[(i,j)] = (0, False)
            if r[i][j] == '@':
                m[(i,j)] = (m[(i,j)][0]+1, m[(i,j)][1])

def count(r):
    m = {}
    recursion(r, 0, 0, m)
    i = len(r)-1
    return m[(i,i)][0] if m[(i,i)][1] else -1


if __name__ == "__main__":
    r = ["....@",
         "@##.#",
         ".##@#",
         ".@..#",
         "###@."]
    print(count(r)) # 2
    a = ["@..@#",
        ".@@@@",
        "@.@#@",
        "..#..",
        "@@.@."]
    print(count(a)) # 4