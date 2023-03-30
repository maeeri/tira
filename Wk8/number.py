def sums(n):
    pass

def count(n):
    if n == 1:
        return 1
    for i in range(n-n//2):
        for j in range(i):
            return count(n-j)
    

if __name__ == "__main__":
    print(count(4)) # 5
    # print(count(5)) # 7
    # print(count(8)) # 22
    # print(count(42)) # 53174