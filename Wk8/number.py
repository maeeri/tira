def sums(n, o, t, temp):
    s = sum(temp)
    if s == o:
        t.add(tuple(temp))
        return
    for i in range(n, 0, -1):
        if s + i > o:
            continue
        temp.append(i)
        sums(i, o, t, temp)
        temp.pop()

def count(n):
    t = set() # set of unique tuples representing sequences
    sums(n, n, t, [])
    return len(t)

if __name__ == "__main__":
    print(count(4)) # 5
    print(count(5)) # 7
    print(count(8)) # 22
    print(count(42)) # 53174
    print(count(50)) # 204226