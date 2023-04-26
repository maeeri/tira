from collections import deque, defaultdict

class Network:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.graph = {(n,m): [] for n in range(self.n) for m in range(self.m)}
        self.box = (0,0)
        self.player = (0,0)
        self.box_target = (0,0)
        self.walls = []

    def add_link(self, a, b):
        self.graph[a].append(b)
        self.graph[b].append(a)

    def is_wall(self, x):
        return x in self.walls

    def get_route(self, visited):
        start = (self.player, self.box, 0)
        q=deque()
        q.append(start)
        visited.add(start)
        steps = defaultdict()

        while q:
            for _ in range(len(q)):
                player_pos, box_pos, depth = q.popleft()
                for new_player_pos in self.graph[player_pos]:
                    box_is_moving = new_player_pos == box_pos
                    new_box_pos = (box_pos[0]+(new_player_pos[0]-player_pos[0]), box_pos[1]+(new_player_pos[1]-player_pos[1])) if box_is_moving else box_pos
                    illegal_move = self.is_wall(new_box_pos) or self.is_wall(new_player_pos)
                    if illegal_move or (new_player_pos, new_box_pos) in visited:
                        continue
                    elif new_box_pos == self.box_target:
                        steps[new_box_pos] = depth + 1
                        return steps[new_box_pos]
                    q.append((new_player_pos, new_box_pos, depth+1))
                    visited.add((new_player_pos, new_box_pos))

        return -1 if self.box_target not in steps else steps[self.box_target]    

def count(r):
    network = Network(len(r), len(r[0]))
    for i in range(len(r)):
        for j in range(len(r[i])):
            if r[i][j] == '#':
                network.walls.append((i,j))
            if r[i][j] == 'X':
                network.player = (i,j)
            if r[i][j] == 'B':
                network.box = (i,j)
            if r[i][j] == 'Y':
                network.box_target = (i,j)
            if i < len(r)-1: network.add_link((i,j),(i+1,j)) 
            if j < len(r[0])-1: network.add_link((i,j),(i,j+1))
    visited = set()
    return network.get_route(visited)

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
        "#........#",
        "#........#",
        "#...Y....#",
        "#...B....#",
        "#...#...##",
        "#........#",
        "#...X...##",
        "#........#",
        "##########"]
    print(count(r))

    r = ["####################",
        "#..#...........#.#.#",
        "#...#..#.#..B#.....#",
        "###...#.#.#...#.#..#",
        "#..#.#.............#",
        "##.#..#............#",
        "#............#.##..#",
        "#.......#...#....###",
        "#....#.....#.......#",
        "#....#.#...........#",
        "#......#........#.##",
        "#..#..#........#...#",
        "#.#.#..........#...#",
        "#.#...........#....#",
        "#.#.#.........#.#..#",
        "#...#..........#...#",
        "#.X#......#......###",
        "#..#.##.#...#.###..#",
        "#.#........Y.......#",
        "####################"]
    print(count(r))