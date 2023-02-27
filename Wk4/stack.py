class Stack:
    def __init__(self):
        self.t = []
        self.sum = sum(self.t)
 
    def push(self, x):
        y = x - self.sum
        self.t.append(y)
        self.sum += y
 
    def pop(self):
        s = self.sum
        x = self.t.pop()
        self.sum -= x
        return s
 
    def increase(self, k):
        self.t[len(self.t)-k] += 1
        self.sum += 1

if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.increase(2)
    print(s.pop()) # 4
    s.push(1)
    s.increase(2)
    print(s.pop()) # 2
    print(s.pop()) # 4
    print(s.pop()) # 1