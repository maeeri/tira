from collections import deque
 
class Network:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.box_graph = {(n,m): [] for n in range(self.n+1) for m in range(self.m+1)}
        self.player_graph = {(n,m): [] for n in range(self.n+1) for m in range(self.m+1)}
        self.box = (0,0)
        self.player = (0,0)
        self.target = (0,0)
 
    def add_link(self, a, b, x=''):
        if x == 'box':
            self.box_graph[a].append(b)
        else:
            self.player_graph[a].append(b)
            self.player_graph[b].append(a)
 
    def route_lenght(self, a, b):
        return len(self.best_route(a, b))
 
    def best_route(self, a, b, box=False):
        self.q = deque()
        self.visited = {(n,m): False for n in range(self.n+1) for m in range(self.m+1)}
        self.paths = {(n,m): [] for n in range(self.n+1) for m in range(self.m+1)}
        self.path = []
        self.bfs(a, box)
        return self.paths[b]
 
    def bfs(self, x, box=False):
        graph = self.box_graph if box else self.player_graph
        self.q.append(x)
        self.visited[x] = True
        while len(self.q) > 0:
            knot = self.q.popleft()
            for y in graph[knot]:
                if self.visited[y]:
                    continue
                if y != self.box:
                    self.q.append(y)
                    self.visited[y] = True
                    self.paths[y] = self.paths[knot] + [y]
 
def count(r):
    network = Network(len(r), len(r[0]))
    floor = ['Y', '.', 'B', 'X']
    for i in range(len(r)):
        for j in range(len(r[i])):
            if r[i][j] in floor:
                if r[i][j-1] in floor:
                    network.add_link((i,j), (i, j-1))
                    if r[i][j+1] in floor:
                        network.add_link((i,j), (i,j-1), 'box')
                        network.add_link((i,j), (i,j+1), 'box')
                if r[i-1][j] in floor:
                    network.add_link((i,j), (i-1, j))
                    if r[i+1][j] in floor:
                        network.add_link((i,j), (i-1,j), 'box')
                        network.add_link((i,j), (i+1,j), 'box')
            if r[i][j] == 'X':
                network.player = (i,j)
            if r[i][j] == 'B':
                network.box = (i,j)
            if r[i][j] == 'Y':
                network.target = (i,j)
    box_route = [network.box] + network.best_route(network.box, network.target, True)
    if len(box_route) == 1:
        return -1
 
    counter = 0
    for i in range(len(box_route)-1):
        fr, to = box_route[i], box_route[i+1]
        if fr[0] < to[0]:
            b = (fr[0]-1,fr[1])
        if fr[0] > to[0]:
            b = (fr[0]+1,fr[1])
        if fr[1] < to[1]:
            b = (fr[0],fr[1]-1)
        if fr[1] > to[1]:
            b = (fr[0],fr[1]+1)
        steps = network.route_lenght(network.player, b)
        if steps == 0 and network.player != b:
            return -1
        counter += steps + 1
        network.player = network.box
        network.box = to
    return counter
 
if __name__ == "__main__":
    r = ["########",
         "#......#",
         "#.#.Y#.#",
         "#.#B.#.#",
         "#..X.#.#",
         "#.#..#.#",
         "########"]
    print(count(r)) # 18
 
    r = ["##########",
        "##...Y...#",
        "#...#....#",
        "##X##....#",
        "##..#...##",
        "#....#...#",
        "#......###",
        "#.##...B.#",
        "##.#.#.#.#",
        "##########"]
    print(count(r)) # -1

    r = ["##########", #0
        "#......Y.#", #1
        "#........#", #2
        "#........#", #3
        "#..#.B...#", #4
        "#..X..#..#", #5
        "#........#", #6
        "#..#.....#", #7
        "#.##.....#", #8
        "##########"] #9
        #0123456789
    print(count(r)) # 9