def create(n, k):
    bits = [*("0" * n)]
    for i in range(1, k+1):
        for j in range(0, n):
            if bits[j] == "0": 
                bits[j] = "1"
                break
            else: 
                bits[j] = "0"
    return "".join(bits)

if __name__ == "__main__":
    print(create(5, 0)) # 00000
    print(create(5, 1)) # 10000
    print(create(5, 2)) # 01000
    print(create(5, 3)) # 11000
    print(create(5, 4)) # 00100
    print(create(5, 31)) # 11111