class Shortening:
    def __init__(self,n):
        self.n = n
        self.graph = [[10**7]*(self.n+1) for _ in range(self.n+1)]
        self.adj = [[] for _ in range(self.n+1)]

    def add_edge(self,a,b,x):
        if self.graph[a][b] > 10**6: self.graph[a][b] = 0
        self.graph[a][b] += x
        self.adj[a].append(b)

    def check(self,a,b):
        self.fw()
        x = self.graph[a][b]
        self.fw()
        y = self.graph[a][b]
        return y < x and y < 0
    
    def dfs(self, a, b, i):
        if self.visited[a]:
            return
        self.visited[a] = True
        if a == b:
            return False
        if a == i:
            return True
        for neighbor in self.adj[a]:
            return self.dfs(neighbor, b, i)

    
    def fw(self):
        for k in range(self.n+1):
            for i in range(self.n+1):
                for j in range(self.n+1):
                    self.graph[i][j] = min(self.graph[i][j], self.graph[i][k]+self.graph[k][j])
 
if __name__ == "__main__":
    s = Shortening(5)
    print(s.check(1,3)) # False
    s.add_edge(1,2,5)
    s.add_edge(2,3,-2)
    print(s.check(1,3)) # False
    s.add_edge(2,4,1)
    s.add_edge(4,2,-2)
    print(s.check(1,3)) # True
   

    
    s = Shortening(5)
    s.add_edge(1,5,6)
    print(s.check(5,4))
    print(s.check(4,5))
    print(s.check(4,5))
    s.add_edge(5,3,-9)
    s.add_edge(1,3,9)
    s.add_edge(2,3,-2)
    s.add_edge(4,3,1)
    print(s.check(5,4))
    print(s.check(5,3))
    s.add_edge(3,1,-6)
    s.add_edge(2,1,-9)
    print(s.check(4,1))
    s.add_edge(5,4,2)
    print(s.check(5,2))
    print(s.check(1,3))
    s.add_edge(3,5,0)
    print(s.check(3,5))
    s.add_edge(1,4,7)
    print(s.check(3,4))