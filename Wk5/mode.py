class Mode:
    def __init__(self):
        self.dict = {}
        self.mode = (0, 0)

    def add(self, x):
        if x not in self.dict.keys():
            self.dict[x] = 1
        else:
            self.dict[x] += 1
        if self.dict[x] >= self.mode[1]:
            if x <= self.mode[0] or self.mode[0] == 0 or self.dict[x] > self.mode[1]:
                self.mode = (x, self.dict[x])
        return self.mode[0]
        

if __name__ == "__main__":
    pass
