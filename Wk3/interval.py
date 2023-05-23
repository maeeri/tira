def count(t):
    x = sorted(list(set(t)))
    counter = 1
    seq = []
    for i in range(1, len(x)):
        if x[i] - x[i-1] == 1:
            counter += 1
        else:
            seq.append(counter)
            counter = 1
    seq.append(counter)
    return max(seq)


if __name__ == "__main__":
    print(count([1, 1, 1, 1])) # 1
    print(count([14, 15, 16, 15, 13])) # 4
    print(count([7, 6, 1, 8])) # 3
    print(count([1, 2, 1, 2, 1, 2])) # 2
    print(count([987654, 12345678, 987653, 999999, 987655])) # 3
    print(count([7, 9, 10, 2, 1, 8])) # 4
    a = list(range(10**6, 10**6 - 10**5, -1))
    print(count(a))

# Annettuna on lista, josta tulee poimia mahdollisimman monta lukua. 
# Ensimmäinen luku saa olla mikä tahansa listan luku ja tämän jälkeen 
# seuraavan poimitun luvun tulee olla tasan yhden suurempi kuin edellinen. 
# Kuinka monta lukua voidaan näin korkeintaan poimia?

# Voit olettaa, että listalla on enintään 105 lukua ja että jokainen luku on väliltä 1…10**9.
# Tavoitteena on, että algoritmin aikavaativuus on O(n) tai O(nlogn).

# Toteuta tiedostoon interval.py funktio count, joka ilmoittaa, montako lukua listalta voidaan 
# enintään poimia halutulla tavalla.