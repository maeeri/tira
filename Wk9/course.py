from math import factorial
from functools import reduce


def ncr(n, k):
    return factorial(n)//(factorial(k)*factorial(n-k))


memory = {35: ncr(8, 5)**7, 54: ncr(56, 54), 55: ncr(56, 55), 56: ncr(56, 56)}


def calculate(x):
    if x in memory:
        return
    memory[x] = ncr(8, x)


def sums(o, t, temp):
    s = sum(temp)
    if s == o and len(temp) < 8:
        t.add(tuple(temp))
        return
    for i in range(3, 0, -1):
        if s + i > o:
            continue
        temp.append(i)
        sums(o, t, temp)
        temp.pop()


def count(x):
    if x > 56 or x < 35:
        return 0

    if x in memory:
        return memory[x]

    for i in range(5, 9):
        calculate(i)

    extras = x-35
    t = set()

    sums(extras, t, [])
    print(len(t))
    print(ncr(56,x)//len(t))
    res = []
    for y in t:
        temp = []
        for i in range(7):
            if len(y) > i:
                temp.append(memory[5+y[i]])
            else:
                temp.append(memory[5])
        print(reduce(lambda a,b: a*b, temp)//len(t))
    print(res)
    return


if __name__ == "__main__":
    # print(count(35)) # 1727094849536 1727094849536
    print(count(42))  # 2375030784000 
                      #  131925726450
    # print(count(55))  # 56
    # print(count(56)) # 1
    # print(count(80)) # 0
