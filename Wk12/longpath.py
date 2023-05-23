from collections import deque

class LongPath:
    def __init__(self,n):
        self.n = n
        self.graph = [[] for _ in range(n+1)]
        self.max_path = 0
        self.change = False

    def add_edge(self,a,b):
        if b > a:
            a,b = b,a
        if b not in self.graph[a]:
            self.graph[a].append(b)
            self.graph[a].sort(reverse=True)
        self.change = True

    def calculate(self):
        if self.change:
            self.longest_paths = {0: 0}
            for i in range(self.n+1):
                self.get_longest_path(i)
        return self.max_path

    def get_longest_path(self, x):
        if len(self.graph[x]) == 0:
            return 0
        if x in self.longest_paths:
            return self.longest_paths[x]
        for neighbor in self.graph[x]:
            new_path = self.get_longest_path(neighbor) + 1
            self.longest_paths[x] = new_path if x not in self.longest_paths else max(self.longest_paths[x], new_path)
        self.max_path = max(self.longest_paths[x], self.max_path)
        return self.longest_paths[x]

if __name__ == "__main__":
    l = LongPath(4)
    l.add_edge(1,2)
    l.add_edge(1,3)
    l.add_edge(2,4)
    l.add_edge(3,4)
    print(l.calculate()) # 2
    l.add_edge(3,2)
    print(l.calculate()) # 3

    l = LongPath(5)
    l.add_edge(4,2)
    print(l.calculate()) # 1
    l.add_edge(4,3) 
    l.add_edge(2,3)
    print(l.calculate()) # 2
    l.add_edge(4,2)
    print(l.calculate()) # 2
    l.add_edge(4,5)
    l.add_edge(1,2)
    print(l.calculate()) # 4

    l = LongPath(5)
    l.add_edge(4,2)
    l.add_edge(5,1)
    l.add_edge(3,5)
    print(l.calculate()) # 1
    print(l.calculate()) # 1
    l.add_edge(3,4)
    l.add_edge(1,5)
    l.add_edge(3,2)
    l.add_edge(1,3)
    print(l.calculate()) # 2

    l = LongPath(50)
    l.add_edge(1,2)
    l.add_edge(2,3)
    l.add_edge(3,4)
    l.add_edge(4,5)
    l.add_edge(5,6)
    l.add_edge(6,7)
    l.add_edge(7,8)
    l.add_edge(8,9)
    l.add_edge(9,10)
    l.add_edge(10,11)
    l.add_edge(11,12)
    l.add_edge(12,13)
    l.add_edge(13,14)
    l.add_edge(14,15)
    l.add_edge(15,16)
    l.add_edge(16,17)
    l.add_edge(17,18)
    l.add_edge(18,19)
    l.add_edge(19,20)
    l.add_edge(20,21)
    l.add_edge(21,22)
    l.add_edge(22,23)
    l.add_edge(23,24)
    l.add_edge(24,25)
    l.add_edge(25,26)
    l.add_edge(26,27)
    l.add_edge(27,28)
    l.add_edge(28,29)
    l.add_edge(29,30)
    l.add_edge(30,31)
    l.add_edge(31,32)
    l.add_edge(32,33)
    l.add_edge(33,34)
    l.add_edge(34,35)
    l.add_edge(35,36)
    l.add_edge(36,37)
    l.add_edge(37,38)
    l.add_edge(38,39)
    l.add_edge(39,40)
    l.add_edge(40,41)
    l.add_edge(41,42)
    l.add_edge(42,43)
    l.add_edge(43,44)
    l.add_edge(44,45)
    l.add_edge(45,46)
    l.add_edge(46,47)
    l.add_edge(47,48)
    l.add_edge(48,49)
    l.add_edge(49,50)
    l.add_edge(1,3)
    l.add_edge(2,4)
    l.add_edge(3,5)
    l.add_edge(4,6)
    l.add_edge(5,7)
    l.add_edge(6,8)
    l.add_edge(7,9)
    l.add_edge(8,10)
    l.add_edge(9,11)
    l.add_edge(10,12)
    l.add_edge(11,13)
    l.add_edge(12,14)
    l.add_edge(13,15)
    l.add_edge(14,16)
    l.add_edge(15,17)
    l.add_edge(16,18)
    l.add_edge(17,19)
    l.add_edge(18,20)
    l.add_edge(19,21)
    l.add_edge(20,22)
    l.add_edge(21,23)
    l.add_edge(22,24)
    l.add_edge(23,25)
    l.add_edge(24,26)
    l.add_edge(25,27)
    l.add_edge(26,28)
    l.add_edge(27,29)
    l.add_edge(28,30)
    l.add_edge(29,31)
    l.add_edge(30,32)
    l.add_edge(31,33)
    l.add_edge(32,34)
    l.add_edge(33,35)
    l.add_edge(34,36)
    l.add_edge(35,37)
    l.add_edge(36,38)
    l.add_edge(37,39)
    l.add_edge(38,40)
    l.add_edge(39,41)
    l.add_edge(40,42)
    l.add_edge(41,43)
    l.add_edge(42,44)
    l.add_edge(43,45)
    l.add_edge(44,46)
    l.add_edge(45,47)
    l.add_edge(46,48)
    l.add_edge(47,49)
    l.add_edge(48,50)
    print(l.calculate()) # 49

# Tehtäväsi on toteuttaa luokka, jonka avulla pystyy lisäämään kaaren suuntaamattomaan verkkoon sekä 
# selvittämään, kuinka pitkä on pisin sellainen polku, jossa jokaisen solmun tunnus on suurempi kuin 
# edellisen solmun tunnus.

# Voit olettaa, että solmuja on enintään 50 ja luokan metodeita kutsutaan enintään 100 kertaa.

# Toteuta tiedostoon longpath.py luokka LongPath, jossa on seuraavat metodit:
# - konstruktori, jolle annetaan solmujen määrä
# - add_edge lisää kaaren kahden solmun välille
# - calculate antaa pisimmän polun pituuden