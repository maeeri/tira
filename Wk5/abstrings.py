def count(a, b):
    l_a = []
    l_b = []
    for i in range(len(a)):
        if a[i] == 'A':
            l_a.append(1)
        if a[i] == 'B':
            l_a.append(-1)
        if b[i] == 'A':
            l_b.append(-1)
        if b[i] == 'B':
            l_b.append(1)
    counter = 0
    for i in range(len(l_a)):
        pass
    return counter


if __name__ == "__main__":
    # print(count("AAA", "BBB")) # 0
    # print(count("AB", "BA")) # 1
    # print(count("AA", "AA")) # 3
    # print(count("ABA", "BAB")) # 2
    # print(count("AAABBB", "BBBAAA")) # 3
    print(count("AABABBBA", "BAABABAB")) # 13
    print(count("A"*(10**5//2)+"B"*(10**5//2), "A"*10**5))