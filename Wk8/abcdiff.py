def create(n):
    l = ["A", "B", "C"]
    if n == 1:
        return l
    else:
        x = create(n-1)
        r = []
        for s in x:
            for c in l:
                if s[-1] != c:
                    r.append(s+c)
        return r

if __name__ == "__main__":
    print(create(1)) # [A,B,C]
    print(create(2)) # [AB,AC,BA,BC,CA,CB]
    print(len(create(5))) # 48

# Tehtäväsi on muodostaa lista, jossa on kaikki n merkin pituiset merkkijonot, 
# joissa jokainen merkki on A, B tai C ja missään kohdassa ei ole vierekkäin kahta samaa merkkiä. 
# Listan tulee olla aakkosjärjestyksessä.

# Voit olettaa, että n on välillä 1…10.

# Toteuta tiedostoon abcdiff.py funktio create, joka muodostaa listan.