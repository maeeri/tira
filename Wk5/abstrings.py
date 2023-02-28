def count(a, b):
    l_a = []
    l_b = []
    for i in range(len(a)):
        l_a.append(alphanum(a[i]))
        l_b.append(-alphanum(b[i]))
    for i in range(len(a)):
        print(l_a[i]+l_b[i])
    return 0

def alphanum(c):
    return 1 if c == 'A' else -1

if __name__ == "__main__":
    print(count("AAA", "BBB")) # 0
    print(count("AB", "BA")) # 1
    print(count("AA", "AA")) # 3
    print(count("ABA", "BAB")) # 2
    print(count("AAABBB", "BBBAAA")) # 3
    # print(count("AABABBBA", "BAABABAB")) # 13
    # print(count("A"*(10**5//2)+"B"*(10**5//2), "A"*10**5))