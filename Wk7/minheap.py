from math import log2, floor, ceil

def count(n, k):
    h = floor(log2(n))
    if k == 1: return 1
    u = sum([2**i for i in range(h-1, -1, -1)])
    left = n % u
    # print(u)
    lvls = {h-i+1:2**(h-i) for i in range(h, -1, -1)}
    
    # print(lvls)
    r = 0
    if k == 1: r = 1
    elif n < 2**2 and k < 4: r = 2
    elif k < n//2+1:
        r = n - 2
    else:
        x = n//2
        if n < 2**3:
            r = 3
        elif n < 2**4:
            r = 6
        elif n < 2**5:
            r = 8
    return r
        



if __name__ == "__main__":
    print(count(1,1)) # 1
    print(count(3,2)) # 2
    print(count(5,4)) # 3
    print(count(5,5)) # 3
    print(count(10,9)) # 6
    print(count(70,34)) # 68
    print(count(100,8))