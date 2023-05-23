def find(t, x):
    t.sort()
    counter = 1
    res = 1
    b = 0
    for i in range(1, len(t)):
        if t[i] - t[b] > x:
            b += 1
        else:
            counter += 1
        res = max(res, counter)
    return res

if __name__ == "__main__":
    print(find([10, 10, 10, 10], 0)) # 4
    print(find([4, 2, 7, 1], 0)) # 1
    print(find([7, 3, 1, 5, 2], 2)) # 3
    print(find([7, 3, 1, 5, 2], 1000)) # 5
    print(find([19, 4, 7, 17, 3, 15, 10], 5)) # 3
    print(find([10000, 987654, 123456, 139562, 13613225], 50000)) # 2
    print(find([2, 7, 14, 11, 7, 15], 11)) # 5


# Annettuna on lista lukuja ja tehtäväsi on selvittää, montako lukua listalta voidaan valita siten, 
# että minkään kahden valitun luvun erotus ei ole suurempi kuin x.

# Voit olettaa, että listalla on enintään 10**5 lukua ja x
# ja jokainen listan luku on väliltä 0…10**9. Tavoitteena on, että algoritmin aikavaativuus on O(n)
# tai O(nlogn).

# Toteuta tiedostoon bigset.py funktio find, joka ilmoittaa montako lukua listalta voidaan enintään valita.

# Selitys: Toisessa esimerkissä listalla [4,2,7,1] kaikki luvut ovat erisuuria, joten voimme valita vain yhden luvun, 
# sillä muuten löytyisi aina lukupari, jonka erotus on suurempi kuin 0. 
# Kolmannessa esimerkissä listalta [7,3,1,5,2] voidaan valita kolme lukua: 3, 1 ja 2
# ja näiden lukujen väliset erot ovat kaikki korkeintaan 2.