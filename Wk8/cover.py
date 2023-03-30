def count(n, m, k):
    if n*m == 1 or k == 1:
        return 1
    else:
        count(n, m, k-1)
        

if __name__ == "__main__":
    print(count(2,2,4)) # 8
    print(count(2,3,3)) # 13
    print(count(4,4,1)) # 1
    print(count(4,3,10)) # 3146
    print(count(4,4,16)) # 70878