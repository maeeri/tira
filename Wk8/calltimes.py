from time import time
c = 0

def f(n):
    global c
    c += 1
    if n <=2:
        return n
    return f(n-1)+f(n-2)+f(n-3)

print(f(30))
print(c)
