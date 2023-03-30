from time import time

def f(n):
    if n <= 2:
        return n
    return f(n-1)+f(n-2)+f(n-3)

b = time()
print(f(30))
e = time()

print(e-b)