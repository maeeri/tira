class Graph:
    def __init__(self, n):
        self.graph = [[] for _ in range(101)]
        self.edges = []

    def add_link(self, a, b):
        self.graph[a].append(b)

    def check(self, x, y):
        pass

def create(x):
    pass

if __name__ == "__main__":
    print(create(2)) # esim. [(1,2),(1,100),(2,100)]
    # print(create(5))
    # print(create(10))
    # print(create(123456789))