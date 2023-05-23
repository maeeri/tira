def create(n):
    a = []
    create_array(1, n, a)
    return a

def get_middle(b, e):
    if (b+(e-b))%2==0:
        return b + (e-b)//2
    return b + (e-b)//2

def create_array(b, e, a):
    m = get_middle(b, e)
    a.append(m)
    if e-m == 1: a.append(e)
    elif e-m > 1: create_array(m+1, e, a)
    if m-b == 1: a.append(b)
    elif m-b > 1: create_array(b, m-1, a)
    

if __name__ == "__main__":
    print(create(1)) # [1]
    print(create(3)) # [2, 3, 1]
    print(create(4)) # [2, 1, 4, 3]
    print(create(7)) # [4, 6, 5, 2, 3, 7, 1]

# Tehtäväsi on selvittää, missä järjestyksessä luvut 1…n tulee lisätä tyhjään binäärihakupuuhun, 
# jotta puun korkeudesta tulee mahdollisimman pieni. Voit antaa minkä tahansa kelvollisen ratkaisun. 
# Voit olettaa, että puussa on enintään 100 solmua.

# Toteuta tiedostoon fillorder.py funktio create, joka palauttaa jonkin lukujen 1…n
#  permutaation, joka minimoi hakupuun korkeuden.

# Selitys: Jos n=3, yksi kelvollinen ratkaisu on laittaa luvut hakupuuhun järjestyksessä [2,3,1]. 
# Tällöin luku 2 asetetaan puun juureksi, luku 3 tämän oikeaksi lapseksi ja luku 1 juuren vasemmaksi 
# lapseksi. Luvut 1 ja 3 päätyvät siis syvyydelle 1. Kuitenkin esimerkiksi järjestys [1,2,3]
# ei olisi kelvollinen. Nyt luku 1 päätyy puun juureksi, 2 tämän oikeaksi lapseksi ja 3 luvun 
# 2 oikeaksi lapseksi. Luku 3 päätyy siis syvyydelle 2, mikä on suurempi kuin minkään solmun 
# syvyys optimaalisessa järjestyksessä.