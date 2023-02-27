from heapq import heappop, heappush, heapify

def find(t, x):
    if t[-1] >= t[0] and t[-1] - t[0] <= x: return len(t)
    a = list((-i, t[i]) for i in range(len(t)))
    b = list((i, t[i]) for i in range(len(t)))
    heapify(a)
    heapify(b)
    temp = [1]
    
    for i in range(len(t)//2+1):
        for j in range(len(t)//2+1):
            print(a[0], b[j])
            if a[0][1] > b[j][1] and a[0][1] - b[j][1] <= x:
                temp.append(len(a)-i-j) 
        heappop(a)
    return max(temp)

if __name__ == "__main__":
    # print(find([1, 4, 6], 1)) # 1
    # print(find([1, 4, 6], 10)) # 3
    print(find([4, 1, 10, 5, 14], 1)) # 4
    # print(find([4, 1, 10, 5, 14], 10)) # 5
    # print(find([9, 8, 7, 6, 5, 4, 3, 2, 1], 100)) # 1
    # print(find([13, 10, 1, 12], 20)) # 3
    # print(find([12, 10, 13, 7], 12)) # 3