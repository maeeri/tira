import math

def count(n, k):
    h = math.ceil(math.log2(n))
    if k <= 2**(h-1):
        return [k]
    else:
        positions = [k]
        while k > 1:
            k //= 2
            positions.append(k)
        return positions[::-1]

if __name__ == "__main__":
    print(count(1,1)) # 1
    print(count(3,2)) # 2
    print(count(5,4)) # 3
    print(count(5,5)) # 3
    print(count(10,9)) # 6
    print(count(70,34)) # 68
    print(count(100,8))