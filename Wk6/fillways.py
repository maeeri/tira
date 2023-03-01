from math import log2, floor, ceil, factorial

def count(n):
    print(ncr(1, 1))
    print(ncr(2, 2))
    print(ncr(4, 1))
    print(ncr(8, 8))
    print(ncr(16, 16))

    return ncr(n, n-1)

def ncr(n, k):
    if k == 0: return 1
    if k > n: return 0
    return factorial(n)//factorial(n-k)

def get_middle(b, e):
    if (b+(e-b))%2==0:
        return b + (e-b)//2
    return b + (e-b)//2

if __name__ == "__main__":
    print(count(1)) # 1
    # print(count(3)) # 2
    # print(count(4)) # 16
    # print(count(7)) # 80
    # print(count(10)) # 253440
    # print(count(31)) # 74836825861835980800000