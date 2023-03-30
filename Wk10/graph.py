edges = {}
for i in range(2, 1000):
    edges[i] = []
    for j in range(3, 1001):
        if i != j and (i%j==0 or j%i==0 and (j,i) not in edges):
            edges[i].append((i,j))
counter = 1
for x in edges:
    z = True
    for y in edges[x]:
        for k in edges:
            if y in edges[k]:
                z = False
    if z: counter += 1

print(counter)