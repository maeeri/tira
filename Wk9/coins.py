
def count(t):
    s = sum(t)
    sums = [False for _ in range(s+1)]
    t.sort()
    sums[t[0]] = True
    counter = 0
    for i in range(len(t)):
        for j in range(s-1,-1,-1):
            if sums[j] and j+t[i] < len(sums):
                sums[j+t[i]] = True
    for i in range(len(sums)):
        if sums[i]:
            counter += 1
    return counter

if __name__ == "__main__":
    print(count([3,4,5])) # 7
    print(count([1,1,2])) # 4
    print(count([2,2,2,3,3,3])) # 13
    print(count([42,5,5,100,1,3,3,7])) # 91

# Sinulla on n kolikkoa ja jokaisella kolikolla on jokin kokonaislukuarvo. 
# Tehtäväsi on laskea, montako eri summaa voit muodostaa käyttämällä kolikoita.

# Esimerkiksi kun kolikot ovat [3,4,5], mahdolliset summat ovat 3, 4, 5, 7, 8, 9 ja 12. 
# Tässä tapauksessa on siis 7 mahdollista summaa. Huomaa, että summassa tulee olla vähintään yksi kolikko eli tyhjä ratkaisu ei kelpaa.

# Voit olettaa, että 1≤n≤100 ja jokaisen kolikon arvo on välillä 1…100

# Toteuta tiedostoon coins.py funktio count, joka antaa mahdollisten summien lukumäärän.