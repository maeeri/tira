def solve(s):
    stack = []
    for c in s:
        stack.append(c)
        while True:
            r = loop(stack)
            if not r: break
    return ''.join(stack)

def loop(stack):
    if len(stack) >= 2 and stack[-2] == stack[-1]:
        stack[-2] = 'a' if stack[-1] == 'z' else chr(ord(stack[-1])+1)
        stack.pop()
        return True
    return False


if __name__ == "__main__":
    print(solve("auto")) # auto
    print(solve("ddqqirr")) # eris
    print(solve("aaaaaa")) # cb
    print(solve("wsstuva")) # xa
    print(solve("zzzzzzzz")) # c
    print(solve("mlkjihgfedcbb")) # n
    print(solve("kkkjjiikjkjiikjjiijkjji")) # mjkjmlki
    s = 'a' * 10**5
    print(solve(s))

# Tehtäväsi on muokata annettua merkkijonoa seuraavalla tavalla:
# Etsi merkkijonosta ensimmäinen kohta, jossa kaksi vierekkäistä merkkiä ovat yhtäsuuria.
# Jos tällaista kohtaa ei ole, lopeta.
# Poista nämä kaksi merkkiä merkkijonosta ja korvaa ne yhdellä merkillä, joka on aakkosissa tasan yhtä suurempi kuin poistetut merkit. Kuitenkin jos uusi merkki olisi suurempi kuin z, siitä tulee merkki a.
# Palaa takaisin kohtaan 1.
# Merkkijono muodostuu merkeistä a–z ja siinä on enintään 10**5 merkkiä.

# Toteuta tiedostoon chars.py funktio solve, joka palauttaa muokatun merkkijonon.