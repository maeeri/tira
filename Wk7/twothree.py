from heapq import heapify, heappop, heappush

def smallest(n):
    t = [1]
    heapify(t)
    for i in range(n):
        x = heappop(t)
        heappush(t, 2*x)
        heappush(t, 3*x)
    return t[0]

if __name__ == "__main__":
    print(smallest(1)) # 2
    print(smallest(5)) # 6
    print(smallest(123)) # 288
    print(smallest(55555)) # 663552