from collections import deque

class Network:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.box_graph = {(n,m): [] for n in range(self.n+1) for m in range(self.m+1)}
        self.player_graph = {(n,m): [] for n in range(self.n+1) for m in range(self.m+1)}
        self.box = (0,0)
        self.player = (0,0)
        self.box_target = (0,0)
        self.player_target = (0,0)
        self.walls = []

    def add_link(self, a, b, x=''):
        if x == 'box':
            self.box_graph[a].append(b)
        else:
            self.player_graph[a].append(b)
            self.player_graph[b].append(a)

    def is_not_wall(self, x):
        return x not in self.walls

    def route_length(self, a, b, visited):
        self.bfs(a, visited)
        return len(self.paths[b])+1

    def best_route(self, a, b, box=False):
        self.q = deque()
        self.visited = {(n,m): False for n in range(self.n+1) for m in range(self.m+1)}
        self.paths = {(n,m): -1 for n in range(self.n+1) for m in range(self.m+1)}
        self.bfs(a)
        return self.paths[b]
    
    def __str__(self) -> str:
        return f"box: {self.box}\nplayer: {self.player}\nbox target: {self.box_target}\nplayer target: {self.player_target}"

    def get_route(self):
        self.q = deque()
        self.q.append((self.box, self.player))
        self.visited = {(n,m,o,p): False for n in range(self.n+1) for m in range(self.m+1) for o in range(self.n+1) for p in range(self.n+1)}
        self.visited[self.box+self.player] = True
        self.paths = {(n,m): -1 for n in range(self.n+1) for m in range(self.m+1)}
        steps = self.bfs()
        print(steps)

    def bfs(self):
        start = (self.player, self.box)
        q=deque()
        visited = set()
        q.append(start)
        visited.add(start)
        steps = {(i,j):0 for i in range(self.n+1) for j in range(self.m+1)}
        temp = 0
        while q:
            for _ in range(len(q)):
                player_pos, box_pos = q.popleft()
                for move in [(0,1), (1,0), (0,-1), (-1,0)]:
                    new_player_pos = (player_pos[0]+move[0], player_pos[1]+move[1])
                    new_box_pos = (box_pos[0] + move[0], box_pos[1] + move[1])
                    if new_box_pos == self.box_target:
                        steps[new_box_pos] = min(temp, steps[box_pos])
                        continue
                    if new_player_pos != new_box_pos and (box_pos, new_player_pos) not in visited and self.is_not_wall(new_player_pos):
                        q.append((box_pos, new_player_pos))
                        visited.add((box_pos, new_player_pos))
                        steps[box_pos] += 1
                    elif new_player_pos == box_pos and (box_pos, new_box_pos) not in visited and self.is_not_wall(new_box_pos):
                        q.append((box_pos, new_box_pos))
                        visited.add((box_pos, new_box_pos))
                        steps[new_box_pos] = min(temp, steps[box_pos]) + 1
                    elif new_box_pos == box_pos and (new_player_pos, new_box_pos) not in visited and self.is_not_wall(new_player_pos):
                        q.append((new_player_pos, new_box_pos))
                        visited.add((new_player_pos, new_box_pos))
                        steps[new_box_pos] = min(temp, steps[box_pos]) + 1
                if box_pos == self.box_target:
                    print(steps)
                    return steps[self.box_target]
                temp += 1
        return -1
        

def count(r):
    network = Network(len(r), len(r[0]))
    floor = ['Y', '.', 'B', 'X']
    wallcounter = 0
    for i in range(len(r)):
        for j in range(len(r[i])):
            if r[i][j] == '#':
                network.walls.append((i,j))
                wallcounter +=1
            else:
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
                network.box_target = (i,j)
    return network.get_route()

if __name__ == "__main__":
    r = ["########",
         "#......#",
         "#.#.Y#.#",
         "#.#B.#.#",
         "#..X.#.#",
         "#.#..#.#",
         "########"]
    print(count(r)) # 18

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