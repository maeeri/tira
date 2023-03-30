class Airports:
    def __init__(self,n):
        self.n = n
        self.graph = [[] for _ in range(self.n+1)]

    def add_link(self,a,b):
        if b not in self.graph[a]: self.graph[a].append(b)

    def check(self):
        for i in range(len(self.graph)):
            for j in range(len(self.graph[i])):
                if i == self.graph[i][j]:
                    return True
        for i in range(1, len(self.graph)):
            visited = [False]*(self.n+1)
            visited[0] = True
            self.dfs(i, visited)
            if False in visited: return False
        return True

    def dfs(self, x, visited):
        if visited[x]:
            return
        visited[x] = True
        for y in self.graph[x]:
            self.dfs(y, visited)

if __name__ == "__main__":
    a = Airports(5)
    a.add_link(1,2)
    a.add_link(2,3)
    a.add_link(1,3)
    a.add_link(4,5)
    print(a.check()) # False
    a.add_link(3,5)
    a.add_link(1,4)
    print(a.check()) # False
    a.add_link(5,1)
    print(a.check()) # True

    a = Airports(5)
    a.add_link(3,1)
    a.add_link(5,4)
    a.add_link(5,4)
    a.add_link(1,5)
    a.add_link(1,4)
    a.add_link(4,5)
    a.add_link(3,1)
    a.add_link(4,3)
    a.add_link(4,2)
    print(a.check()) # False