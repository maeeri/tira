class QuickList:
    def __init__(self, t):
        self.t = t
        self.i = 0

    def move(self, k):
        self.i = (self.i + k)%len(self.t)

    def get(self, i):
        index = (self.i + i)%len(self.t)
        return self.t[index]

if __name__ == "__main__":
    q = QuickList([1,2,3,4,5,6,7,8,9,10])
    print(q.get(4)) # 5
    q.move(3)
    print(q.get(4)) # 8
    q.move(3)
    print(q.get(4)) # 1
    q.move(10)
    print(q.get(4)) # 1
    q.move(7)
    q.move(5)
    print(q.get(0)) # 9
    q = QuickList(list(range(1, 10**5 + 1)))
    for i in range(10**5 - 1):
        q.move(10**5 - 1)
    print(q.get(10**4))