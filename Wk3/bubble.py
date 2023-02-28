from random import shuffle

def count(t):
    if t == sorted(t): return 0
    most = 1
    for i in range(len(t)):
        if i > t[i]: most = max(most, i-t[i]+1)
    return most

if __name__ == "__main__":
    print(count([1, 2, 3])) # 0
    print(count([2, 3, 4, 1])) # 3
    print(count([5, 1, 2, 3, 4])) # 1
    print(count([6, 2, 4, 1, 5, 3])) # 3
    print(count([2, 7, 4, 1, 9, 3, 8, 6, 5, 10])) # 4