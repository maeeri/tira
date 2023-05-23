class CoursePlan:
    def __init__(self):
        self.courses = []
        self.prerequisites = {}
        self.paths = []

    def add_course(self,course):
        self.courses.append(course)
        self.prerequisites[course] = []

    def add_requisite(self,course1,course2):
        self.prerequisites[course2].append(course1)

    def find(self):
        for course in self.prerequisites:
            for i in range(len(self.prerequisites[course])):
                if course == self.prerequisites[course][i]:
                    return
        visited = {course: False for course in self.courses}
        l = []
        for course in self.prerequisites:
            self.dfs(course, visited, l)
        visited = {course: False for course in self.courses}
        r = []
        for course in l:
            l2 = []
            self.dfs(course, visited, l2)
            if len(l2) > 1:
                return
            r += l2
        return r

    def dfs(self, x, visited, l):
        if visited[x]:
            return
        visited[x] = True
        for y in self.prerequisites[x]:
            self.dfs(y, visited, l)
        l.append(x)


if __name__ == "__main__":
    c = CoursePlan()
    c.add_course("Ohpe")
    c.add_course("Ohja")
    c.add_course("Tira")
    c.add_course("Jym")
    c.add_requisite("Ohpe","Ohja")
    c.add_requisite("Ohja","Tira")
    c.add_requisite("Jym","Tira")
    print(c.find()) # [Ohpe,Jym,Ohja,Tira]
    c.add_requisite("Tira","Tira")
    print(c.find()) # None

    c = CoursePlan()
    print(c.find())
    c.add_course('course3')
    c.add_course('course4')
    c.add_requisite('course3','course4')
    c.add_requisite('course4','course3')
    c.add_course('course1')
    c.add_requisite('course4','course1')
    print(c.find())

# Tehtäväsi on toteuttaa luokka, jossa voi määritellä kursseja ja niiden välisiä esitietovaatimuksia 
# sekä etsiä tavan suorittaa kurssit vaatimusten mukaisessa järjestyksessä.

# Jos mahdollisia suoritustapoja on useita, mikä tahansa niistä hyväksytään.

# Voit olettaa, että kursseja on enintään 50 ja luokan metodeita kutsutaan enintään 100 kertaa. 
# Jokaisen kurssin nimi on merkkijono, jossa on enintään 10 merkkiä.

# Toteuta tiedostoon courseplan.py luokka CoursePlan, jossa on seuraavat metodit:
# - konstruktori
# - add_course lisää annetun nimisen kurssin
# - add_requisite lisää esitietovaatimuksen
# - find etsii jonkin tavan suorittaa kurssit ja palauttaa järjestyksen listana 
#   (jos mitään tapaa ei ole, metodi palauttaa None)