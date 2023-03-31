from random import randint, choice

n = 100

link = list(range(n+1))
size = [1]*(n+1)

def find(x):
    while link[x] != x:
         x = link[x]
    return x

def union(a,b):
    a = find(a)
    b = find(b)
    if a == b:
        return
    if size[a] < size[b]:
        a, b = b, a
    size[a] += size[b]
    link[b] = a

for i in range(1,n):
    a = randint(1,n)
    b = randint(1,n)
    union(a,b)

print(len(link), len(set(link)))

for i in range(n):
    x = list(set(link))
    union(choice(x), choice(x))

print(len(link), len(set(link)))
for i in range(1,n+1):
    print(i, ':', link[i], size[i])
root = find(55)
print(find(root))
print(find(8))
print(find(2))