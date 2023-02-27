from random import randint
from time import time
from heapq import heappop, heapify


def organize(t):
    c = sorted(t)
    return sum(c[:len(t)//10])

def stack(t):
    heapify(t)
    sum = 0
    for i in range(len(t)//10):
        sum += heappop(t)
    return sum

if __name__ =="__main__":
    n = 10**6 + 1
    t = []
    for i in range(1, n):
        t.append(randint(1, 10**9))

    begin = time()
    print(organize(t))
    middle = time()
    print(stack(t))
    end = time()

    print(middle-begin)
    print(end-middle)