from random import shuffle

def create(n):
    n_list = list(i for i in range(n, 0, -1))
    return n_list
        

if __name__ == "__main__":
    print(create(6)) # [3, 1, 6, 2, 4, 5]
    print(create(10)) # [7, 10, 3, 1, 5, 4, 8, 6, 9, 2]
    print(create(1005)) # [9, 4, 6, 14, 15, 13, 12, 11, 5, 2, 3, 8, 1, 7, 10]

# Tehtäväsi on järjestää luvut 1…n
#  siten, että kaikkien vierekkäisten lukuparien summat ovat erisuuria. Voit antaa minkä tahansa kelvollisen ratkaisun.

# Voit olettaa, että n
#  on välillä 1…100
# .

# Toteuta tiedostoon permutation.py funktio create, joka palauttaa listan luvuista 1…n
# , jossa kaikkien vierekkäisten lukuparien summat ovat erisuuria.

# Selitys: Koodipohjan esimerkissä [3,1,6,2,4,5], vierekkäisten lukujen summat ovat 4, 7, 8, 6 ja 9. 
# Koska kaikki nämä luvut ovat erisuuria, on ratkaisu kelvollinen. Kuitenkaan esimerkiksi [1,5,2,6,4,3]
#  ei olisi kelvollinen ratkaisu, sillä 5+2=7 ja 4+3=7.