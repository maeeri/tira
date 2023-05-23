from random import shuffle

def count(t):
    if t == sorted(t): return 0
    most = 1
    for i in range(len(t)):
        if i > t[i]: most = max(most, i-t[i]+1)
    return most

if __name__ == "__main__":
    print(count([1, 2, 3])) # 0
    print(count([2, 3, 4, 1])) # 3
    print(count([5, 1, 2, 3, 4])) # 1
    print(count([6, 2, 4, 1, 5, 3])) # 3
    print(count([2, 7, 4, 1, 9, 3, 8, 6, 5, 10])) # 4

# Kuplajärjestäminen on järjestämisalgoritmi, joka koostuu vaihtelevasta määrästä kierroksia. 
# Yhdellä kierroksella lista käydään läpi vasemmalta oikealle ja vierekkäisten lukujen paikkoja 
# vaihdetaan keskenään, mikäli oikeanpuolimmainen on pienempi kuin vasemmanpuolimmainen. 
# Kierroksia suoritetaan, kunnes lista on järjestyksessä.

# Kuplajärjestäminen voidaan toteuttaa Pythonilla näin:

# def bubble(t):
#     while True:
#         change = False
#         for i in range(len(t)-1):
#             if t[i] > t[i+1]:
#                 t[i], t[i+1] = t[i+1], t[i]
#                 change = True
#         if not change:
#             break

# Annettuna on lista, jossa on jokin lukujen 1…n permutaatio, ja tehtäväsi on selvittää, 
# montako kierrosta kuplajärjestämisalgoritmi tarvitsee listan järjestämiseen. Huomaa, että tässä 
# lasketaan vain kierrokset, joiden aikana listan järjestys muuttuu.

# Voit olettaa, että listalla on enintään 105 lukua. Tavoitteena on, että algoritmin aikavaativuus on 
# O(n) tai O(nlogn).

# Toteuta tiedostoon bubble.py funktio count, joka ilmoittaa, montako kierrosta kuplajärjestäminen 
# tarvitsee listan järjestämiseen.