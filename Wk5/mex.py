class Mex:
    def __init__(self):
        self.dict = {}
        self.smallest = 0
        self.keys = set(self.dict.keys())

    def add(self, x):
        if self.dict.get(x) is None:
            self.dict[x] = 1
        else:
            self.dict[x] += 1

        print(x, self.smallest)
        if x == self.smallest and len(self.dict) > self.smallest:
            for i in range(x, 10**9):
                if self.dict.get(i) is None:
                    self.smallest = i
                    break
        elif x == self.smallest: self.smallest = x + 1
        return self.smallest

                

if __name__ == "__main__":
    m = Mex()
    print(m.add(1)) # 0
    print(m.add(3)) # 0
    print(m.add(4)) # 0
    print(m.add(0)) # 2
    print(m.add(5)) # 2
    print(m.add(2)) # 6    
    # m = Mex
    # for i in range(10**5 -2, -1, -1):
    #     m.add(i)
    # print(m.add(10**5-1))