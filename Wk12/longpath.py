class LongPath:
    def __init__(self,n):
        self.n = n
        self.graph = [set() for _ in range(n+1)]
        self.paths = {i: [] for i in range(1, self.n +1)}
        self.max_path = 0

    def add_edge(self,a,b):
        self.graph[a].add(b)
        self.graph[b].add(a)

    def calculate(self):
        self.get_paths()
        return self.max_path

    def get_paths(self):
        for x in range(1, len(self.graph)):
            for y in self.graph[x]:
                if y > x:
                    self.visited = [False] * (self.n+1)
                    self.visited[x] = True
                    l = []
                    self.dfs(y, l)
                    
        self.change = False

    def dfs(self, x, l=[]):
        if self.visited[x]:
            return
        self.visited[x] = True
        l.append(x)
        if len(self.graph[x]) == 0 or x > sorted(list(self.graph[x]), reverse=True)[0]:
            l.reverse()
            if len(l) > 0 and tuple(l) not in self.paths[x]: 
                self.paths[x].append(tuple(l))
                self.max_path = max(len(l), self.max_path)
        for y in self.graph[x]:
            if y > x:
                self.dfs(y, l)
        l.pop()

        

if __name__ == "__main__":
    # l = LongPath(4)
    # l.add_edge(1,2)
    # l.add_edge(1,3)
    # l.add_edge(2,4)
    # l.add_edge(3,4)
    # print(l.calculate()) # 2
    # l.add_edge(3,2)
    # print(l.calculate()) # 3
    
    # l = LongPath(5)
    # l.add_edge(4,2)
    # print(l.calculate())
    # l.add_edge(4,3)
    # l.add_edge(2,3)
    # print(l.calculate())
    # l.add_edge(4,2)
    # print(l.calculate())
    # l.add_edge(4,5)
    # l.add_edge(1,2)
    # print(l.calculate())
    
    # l = LongPath(5)
    # l.add_edge(4,2)
    # l.add_edge(5,1)
    # l.add_edge(3,5)
    # print(l.calculate()) # 1
    # print(l.calculate()) # 1
    # l.add_edge(3,4)
    # l.add_edge(1,5)
    # l.add_edge(3,2)
    # l.add_edge(1,3)
    # print(l.calculate()) # 2

    
    
    
    l = LongPath(50)
    print(l.calculate())
    l.add_edge(24,23)
    l.add_edge(42,21)
    print(l.calculate())
    l.add_edge(5,38)
    l.add_edge(49,50)
    l.add_edge(48,50)
    l.add_edge(47,50)
    print(l.calculate())
    print(l.calculate())
    print(l.calculate())
    l.add_edge(16,23)
    print(l.calculate())
    l.add_edge(9,21)
    l.add_edge(33,22)
    print(l.calculate())
    print(l.calculate())
    print(l.calculate())
    l.add_edge(37,43)
    l.add_edge(50,38)
    print(l.calculate())
    print(l.calculate())
    print(l.calculate())
    l.add_edge(17,45)
    print(l.calculate())
    l.add_edge(34,23)
    l.add_edge(18,17)
    l.add_edge(39,48)
    l.add_edge(42,48)
    print(l.calculate())
    l.add_edge(49,48)
    print(l.calculate())
    print(l.calculate())
    print(l.calculate())
    print(l.calculate())
    l.add_edge(8,32)
    l.add_edge(47,31)
    l.add_edge(12,20)
    print(l.calculate())
    l.add_edge(24,21)
    l.add_edge(25,13)
    print(l.calculate())
    print(l.calculate())
    print(l.calculate())
    print(l.calculate())
    l.add_edge(43,33)
    l.add_edge(38,23)
    l.add_edge(32,44)
    print(l.calculate())
    l.add_edge(31,27)
    l.add_edge(39,7)
    print(l.calculate())
    l.add_edge(35,33)
    l.add_edge(34,31)
    l.add_edge(16,15)
    l.add_edge(32,16)
    print(l.calculate())
    l.add_edge(10,4)
    l.add_edge(25,46)
    l.add_edge(34,37)
    l.add_edge(4,42)
    l.add_edge(50,46)
    print(l.calculate())
    l.add_edge(31,45)
    l.add_edge(47,37)
    print(l.calculate())
    print(l.calculate())
    l.add_edge(39,43)
    l.add_edge(35,43)
    l.add_edge(14,20)
    l.add_edge(29,38)
    l.add_edge(25,37)
    print(l.calculate())
    print(l.calculate())
    print(l.calculate())
    print(l.calculate())
    l.add_edge(48,35)
    print(l.calculate())
    print(l.calculate())
    l.add_edge(29,34)
    l.add_edge(47,33)
    print(l.calculate())
    l.add_edge(16,46)
    print(l.calculate())
    l.add_edge(50,48)
    print(l.calculate())
    l.add_edge(11,50)
    l.add_edge(46,43)
    print(l.calculate())
    for i in l.paths:
        for path in l.paths[i]:
            print(path)
    for i in range(len(l.graph)):
        print(i, l.graph[i])
    l.add_edge(50,43)
    l.add_edge(4,11)
    l.add_edge(36,10)
    l.add_edge(38,21)
    l.add_edge(33,36)
    l.add_edge(43,26)
    l.add_edge(21,44)
    l.add_edge(32,33)
    l.add_edge(17,38)
    print(l.calculate())
    l.add_edge(50,49)