def count(n, m, k):
    pass

if __name__ == "__main__":
    print(count(2,2,4)) # 8
    print(count(2,3,3)) # 13
    print(count(4,4,1)) # 1
    print(count(4,3,10)) # 3146
    print(count(4,4,16)) # 70878

# Tehtäväsi on laskea, monellako tavalla n×m
# suorakulmio voidaan peittää käyttämällä korkeintaan k
# suorakulmiota. Kaikissa suorakulmioissa sivujen pituudet ovat kokonaislukuja.

# Esimerkiksi 2×3 suorakulmio voidaan peittää yhteensä 13
# tavalla, kun suorakulmioita saa käyttää korkeintaan 3

# Voit olettaa, että n ja m ovat välillä 1…4 ja k on välillä 1…nm.

# Toteuta tiedostoon cover.py funktio count, joka antaa peittotapojen määrän.