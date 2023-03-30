def paths(x):
    if x == 1:
        return 1
    if x in temp:
        return temp[x]
    count = 0
    for y in graph[x]:
        count += paths(y)
    temp[x] = count
    return count

n = 1001
graph = [[] for _ in range(1+n)]

temp = {1: 1}
for i in range(n):
    for j in range(i):
        graph[i].append(j)

print(paths(999))