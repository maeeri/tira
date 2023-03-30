class Partition:
    def __init__(self, t):
        self.t = t
        self.subsets = []
        self.get_subsets('')
        self.b = False
                
    def get_subsets(self, c):
        if len(c) == len(self.t):
            self.subsets.append(c)
        else:
            self.get_subsets(c+'0')
            self.get_subsets(c+'1')

    def compare(self):
        for i in range(len(self.subsets)):
            t1 = [self.t[j] for j in range(len(self.t)) if self.subsets[i][j] == '1']
            t2 = [self.t[j] for j in range(len(self.t)) if self.subsets[i][j] == '0']
            if sum(t1) == sum(t2): 
                self.b = True
                break
        

def check(t):
    p = Partition(t)
    p.compare()
    return p.b
    
    

if __name__ == "__main__":
    print(check([3,4,5])) # False
    print(check([16,8,4,4])) # True
    print(check([9,4,8,7,6])) # True
    print(check([1,2,3,4,5,6])) # False
    print(check([1,2,3,4,5,6,7])) # True
    print(check([4,4,4,6,6])) # True
    print(check([22179872, 328807557, 162894491, 212723287, 73679524, 16763251, 20424809, 72619960, 132613455, 254391424, 6116420, 67192881, 252086084, 313755177, 121924316]))
