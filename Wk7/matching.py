from heapq import heapify

def count(a, b):
    heapify(a)
    b.sort()
    print(a, b)
    matches = {}


if __name__ == "__main__":
    print(count([(4,6)], [1, 7])) # 0
    print(count([(2,9), (1,8)], [5])) # 1
    print(count([(1,5), (6,8)], [5, 2])) # 1
    print(count([(6,6), (3,8), (2,5)], [4, 6, 5])) # 3
    print(count([(4,7), (2,6), (8,9), (1,10)], [11, 3, 8, 2, 6])) # 4
    print(count([(4,7), (2,6), (8,9), (5,7)], [11, 3, 8, 2, 6])) # 3