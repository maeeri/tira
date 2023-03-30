from collections import namedtuple
from random import randint, shuffle
import math
from time import time

beginning = time()

Edge = namedtuple("edge", ["beginning", "end", "weight"])
edges = []
distance = {1: 0}

for n in range(1, 5001):
    if n > 9:
        for i in range(n-9, n):
            e = Edge(i, n, randint(1, 1000))
            edges.append(e)
    else:
        for i in range(1, n):
            e = Edge(i, n, randint(1, 1000))
            edges.append(e)
    distance[n] = float(math.inf) if n > 1 else 0
shuffle(edges)

while True:
    change = False
    for edge in edges:
        current = distance[edge.end]
        new = distance[edge.beginning]+edge.weight
        if new < current:
            distance[edge.end] = new
            change = True
    if not change:
        break
print(time()-beginning)