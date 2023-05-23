# ei toimi vielä

def find(s, k):
    a = []
    b = []

    if len(s) == k*3: return k*3

    for i in range(len(s)):
        a.append(s[i])
        b.append(s[len(s)-1-i])


    dict = {'a': [], 'b': [], 'c': []}

    for i in range(len(a)//2+1):
        dict[a[i]].append(i)
        if i != len(a)-i-1: dict[b[i]].append(len(a)-i-1)

    largest = 0
    smallest = 0
    dict["a"].sort()
    dict["b"].sort()
    dict["c"].sort()
    print(dict)

    smallest = max(dict["a"][0], dict["b"][0], dict["c"][0])
    largest = min(dict["a"][-1], dict["b"][-1], dict["c"][-1])
    print(smallest, largest)

if __name__ == "__main__":
    print(find("abc", 1)) # 3
    print(find("aabca", 1)) # 3
    print(find("aaaabbbcccc", 1)) # 6
    print(find("aabbaacc", 2)) # 6
    print(find("aaaabbbbaaaccccaaccacbbaa", 3)) # 13

# Sinulle annetaan merkkijono, joka koostuu vain merkeistä a, b tai c. Voit kerätä merkkejä merkkijonosta poistamalla niitä joko merkkijonon alusta tai lopusta. Kuinka monta merkkiä on vähintään poistettava, jotta jokaista merkkiä a–c saadaan kerättyä vähintään k
#  kappaletta?

# Voit olettaa, että merkkijono muodostuu merkeistä a–c, siinä on enintään 105
#  merkkiä ja kutakin merkkiä on vähintään k
#  kappaletta. Tavoitteena on, että algoritmin aikavaativuus on O(n).

# Toteuta tiedostoon removals.py funktio find, joka kertoo, montako merkkiä on vähintään poistettava.