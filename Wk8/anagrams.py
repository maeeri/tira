def get_anagrams(res, s, o):
    if len(s) == len(o) and s not in res:
        res.append(s)
    else:
        for i in range(len(o)):
            if s.count(o[i]) < o.count(o[i]): get_anagrams(res, s+o[i], o)

def create(s):
    r = []
    get_anagrams(r, '', s)
    return sorted(r)


if __name__ == "__main__":
    print(create("ab")) # [ab,ba]
    print(create("abac")) # [aabc,aacb,abac,abca,acab,acba,baac,baca,bcaa,caab,caba,cbaa]
    print(len(create("aybabtu"))) # 1260

# Tehtäväsi on muodostaa lista, jossa on kaikki annetun merkkijonon anagrammit eli kaikki merkkijonot, 
# jotka voidaan muodostaa merkkijonon merkeistä. Listan tulee olla aakkosjärjestyksessä.

# Voit olettaa, että merkkijono muodostuu merkeistä a–z ja siinä on enintään 8 merkkiä.

# Toteuta tiedostoon anagrams.py funktio create, joka muodostaa listan.