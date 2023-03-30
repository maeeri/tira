
def count(t):
    s = sum(t)
    sums = [False for _ in range(s+1)]
    t.sort()
    sums[t[0]] = True
    counter = 0
    for i in range(len(t)):
        for j in range(s-1,-1,-1):
            if sums[j] and j+t[i] < len(sums):
                sums[j+t[i]] = True
    for i in range(len(sums)):
        if sums[i]:
            counter += 1
    return counter

if __name__ == "__main__":
    print(count([3,4,5])) # 7
    print(count([1,1,2])) # 4
    print(count([2,2,2,3,3,3])) # 13
    print(count([42,5,5,100,1,3,3,7])) # 91