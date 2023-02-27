def count(t):
    x = sorted(list(set(t)))
    counter = 1
    seq = []
    for i in range(1, len(x)):
        if x[i] - x[i-1] == 1:
            counter += 1
        else:
            seq.append(counter)
            counter = 1
    seq.append(counter)
    return max(seq)


if __name__ == "__main__":
    print(count([1, 1, 1, 1])) # 1
    print(count([14, 15, 16, 15, 13])) # 4
    print(count([7, 6, 1, 8])) # 3
    print(count([1, 2, 1, 2, 1, 2])) # 2
    print(count([987654, 12345678, 987653, 999999, 987655])) # 3
    print(count([7, 9, 10, 2, 1, 8])) # 4
    a = list(range(10**6, 10**6 - 10**5, -1))
    print(count(a))