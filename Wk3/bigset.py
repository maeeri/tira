def find(t, x):
    t.sort()
    counter = 1
    res = 1
    b = 0
    for i in range(1, len(t)):
        if t[i] - t[b] > x:
            b += 1
        else:
            counter += 1
        res = max(res, counter)
    return res

if __name__ == "__main__":
    print(find([10, 10, 10, 10], 0)) # 4
    print(find([4, 2, 7, 1], 0)) # 1
    print(find([7, 3, 1, 5, 2], 2)) # 3
    print(find([7, 3, 1, 5, 2], 1000)) # 5
    print(find([19, 4, 7, 17, 3, 15, 10], 5)) # 3
    print(find([10000, 987654, 123456, 139562, 13613225], 50000)) # 2
    print(find([2, 7, 14, 11, 7, 15], 11)) # 5