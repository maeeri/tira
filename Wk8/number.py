def sums(n, o, t, temp):
    s = sum(temp)
    if s == o:
        t.add(tuple(temp))
        return
    for i in range(n, 0, -1):
        if s + i > o:
            continue
        temp.append(i)
        sums(i, o, t, temp)
        temp.pop()

def count(n):
    t = set() # set of unique tuples representing sequences
    sums(n, n, t, [])
    return len(t)

if __name__ == "__main__":
    print(count(4)) # 5
    print(count(5)) # 7
    print(count(8)) # 22
    print(count(42)) # 53174
    print(count(50)) # 204226

# Monellako tavalla kokonaisluku n voidaan esittää positiivisten kokonaislukujen summana? 
# Kaksi tapaa ovat erilaiset, jos summat eroavat, kun luvut järjestetään pienimmästä suurimpaan. 
# Summassa voi olla myös vain yksi luku.

# Esimerkiksi luku 5 voidaan esittää seuraavilla tavoilla: 5, 1+4, 2+3, 1+1+3, 1+2+2, 1+1+1+2 ja 
# 1+1+1+1+1.

# Voit olettaa, että n on välillä 1…50. Koodisi tulee laskea vastaus itse (eli siinä ei saa olla 
# esimerkiksi listaa, jossa on valmiit vastaukset joka testiin).

# Toteuta tiedostoon number.py funktio count, joka antaa esitystapojen määrän.