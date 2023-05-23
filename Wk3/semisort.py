def solve(t):
    counter = 0
    middle = len(t)//2
    for i in range(middle+1):
        if t[i] > middle:
            counter += middle-i
    for i in range(middle, len(t)):
        if t[i] < middle+1:
            counter += i-middle
    return counter

if __name__ == "__main__":
    print(solve([2, 1, 4, 3])) # 0
    print(solve([5, 3, 4, 1, 6, 2])) # 6
    print(solve([6, 5, 4, 3, 2, 1])) # 9
    print(solve([10, 1, 9, 2, 8, 3, 7, 4, 6, 5])) # 15


# Annettuna on lista, jossa on jokin lukujen 1…n permutaatio, jossa n on parillinen. 
# Saat jokaisella siirrolla vaihtaa kaksi vierekkäistä lukua keskenään. 
# Tehtäväsi on järjestää lista siten, että listan puolivälistä katsottuna kaikki alkupuolen luvut 
# ovat pienempiä kuin kaikki loppupuolen luvut. Mikä on pienin määrä siirtoja?

# Voit olettaa, että n on enintään 10**5. Tavoitteena on, että algoritmin aikavaativuus on O(n) tai O(nlogn).

# Toteuta tiedostoon semisort.py funktio solve, joka antaa pienimmän siirtojen määrän.