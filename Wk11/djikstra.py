from random import randint, shuffle
import math
from time import time
from heapq import heappush, heappop

beginning = time()

class Node:
    def __init__(self, id, weight, visited, distance=math.inf):
        self.id = id
        self.weight = weight
        self.visited = visited
        self.adj_list = []
        self.distance = distance

    def add_edge(self, node):
        self.adj_list.append(node)
        shuffle(self.adj_list)

nodes = [Node(1, randint(1, 1000), False, 0)]
heap = []

for n in range(2, 5001):
    if n > 9:
        for i in range(n-9, n):
            e = Node(n, randint(1, 1000), False)
            nodes.append(e)
            nodes[i-1].add_edge(e)
    else:
        for i in range(1, n):
            e = Node(n, randint(1, 1000), False)
            nodes.append(e)
            nodes[i-1].add_edge(e)

b = time()

heappush(heap, (0, nodes[0].id))

while len(heap) > 0:
    item = heappop(heap)
    id = item[1]
    distance = item[0]
    knot = nodes[id-1]
    if knot.visited:
        continue
    knot.visited = True
    for edge in knot.adj_list:
        current = edge.distance
        new = distance + edge.weight
        if new < current:
            distance = new
            heappush(heap, (new, edge.id))

print(time()-b)
