
class GraphGame:
    def __init__(self,n):
        self.n = n
        self.graph = [[] for _ in range(self.n+1)]
        self.paths = {i: [] for i in range(1, self.n +1)}
        self.win = {i: None for i in range(1, self.n+1)}
        self.change = False

    def add_link(self,a,b):
        if b not in self.graph[a]:
            self.graph[a].append(b)
            self.change = True

    def dfs(self, x, l, visited):
        if visited[x]:
            return
        visited[x] = True
        for y in self.graph[x]:
            self.dfs(y, l, visited)
        l.append(x)

    def get_paths(self):
        for x in range(1, len(self.graph)):
            for y in self.graph[x]:
                l = []
                visited = [False]*(len(self.graph)+1)
                self.dfs(y, l, visited)
                l.reverse()
                if len(l) > 0 and tuple(l) not in self.paths[x]: self.paths[x].append(tuple(l))
        self.change = False

    def winning(self,x):
        if self.change:
            self.win = {i: None for i in range(1, self.n+1)}
        self.get_paths()
        self.play_game(x)
        self.change = False
        return self.win[x]

    def play_game(self, x):
        if self.win[x] is not None:
            return self.win[x]
        if len(self.paths[x]) == 0:
            self.win[x] = False
            return False
        if len(self.paths[x]) == 1:
            self.win[x] = not self.play_game(self.paths[x][0][0])
            return self.win[x]
        for y in self.paths[x]:
            b = self.play_game(y[0])
            if not b:
                self.win[x] = True
                break
        self.win[x] = self.win[x] == True
        return self.win[x]

if __name__ == "__main__":
    g = GraphGame(6)
    g.add_link(3,4)
    g.add_link(1,4)
    g.add_link(4,5)
    print(g.winning(3)) # False
    print(g.winning(1)) # False
    g.add_link(3,1)
    g.add_link(4,6)
    g.add_link(6,5)
    print(g.winning(3)) # True
    print(g.winning(1)) # False
    print(g.winning(2)) # False    


# Tarkastellaan kahden pelaajan peliä suunnatussa syklittömässä verkossa. Alussa pelinappula on tietyssä 
# solmussa, ja pelaajat siirtävät vuorotellen nappulan johonkin solmuun, johon pääsee suoraan kaarella 
# nykyisestä solmusta. Peli jatkuu, kunnes pelaaja ei voi tehdä mitään siirtoa, jolloin hän häviää pelin 
# ja toinen pelaaja voittaa.

# Tehtäväsi on toteuttaa luokka, jonka avulla voi lisätä kaaria verkkoon ja selvittää, onko aloittavan 
# pelaajan mahdollista voittaa peli, jos aloitussolmu on x ja molemmat pelaajat pelaavat optimaalisesti.

# Voit olettaa, että solmuja on enintään 50 ja luokan metodeita kutsutaan enintään 200 kertaa.

# Toteuta tiedostoon graphgame.py luokka GraphGame, jossa on seuraavat metodit:
# - konstruktori, jolle annetaan solmujen määrä
# - add_link lisää kaaren solmusta a solmuun b
# - winning kertoo, voittaako aloittaja pelin solmusta x