from heapq import heapify, heappush, heappop
 
def count(a, b):
    heap = []
    b.sort()
    counter = 0
    for x in a:
        heappush(heap, (x[1], x))
    
    print(heap)
 
    for i in range(len(heap)):
        for j in len(b):
            if heap[i][1][0] <= b[j] <= heap[i][1][1]:
                
                pass
    
    return counter



if __name__ == "__main__":
    print(count([(4,6)], [1, 7])) # 0
    print(count([(2,9), (1,8)], [5])) # 1
    print(count([(1,5), (6,8)], [5, 2])) # 1
    print(count([(6,6), (3,8), (2,5)], [4, 6, 5])) # 3
    print(count([(4,7), (2,6), (8,9), (1,10)], [11, 3, 8, 2, 6])) # 4
    print(count([(4,7), (2,6), (8,9), (5,7)], [11, 3, 8, 2, 6])) # 3
    print(count([(8, 17), (13, 16), (4, 12)], [2, 1, 8, 17, 20])) # 2