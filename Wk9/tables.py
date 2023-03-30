from time import time
def f(n):
    r = []
    for i in range(3):
        r.append(i)
    for i in range(3, n+1):
        r.append(r[i-1] + r[i-2] + r[i-3])
    return r[n]

b = time()
print(f(30))
e = time()
print(e-b)