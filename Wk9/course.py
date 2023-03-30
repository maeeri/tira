from math import factorial

memory = {}

def ncr(n, k):
    return factorial(n)//(factorial(n-k)*factorial(k))


def count(x):
    r = [[0]*8 for _ in range(9)]
    if x > 56 or x < 35:
        return 0
    if x in memory:
        return memory[x]
    courseparts = ncr(8, 5)
    memory[35] = courseparts**7
    for i in range(36, 57):
        e = i-35
        print(i, ':', ncr(56, i))
    print(memory)
    print(ncr(56, 42)//memory[35])


if __name__ == "__main__":
    # print(count(35)) # 1727094849536 1727094849536
    print(count(42)) # 2375030784000 5804731963800
    # print(count(55)) # 56
    # print(count(56)) # 1
    # print(count(80)) # 0
