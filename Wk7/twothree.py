from heapq import heappop, heappush

def smallest(n):
    t = [1]
    for i in range(n):
        x = heappop(t)
        heappush(t, 2*x)
        heappush(t, 3*x)
    return t[0]

if __name__ == "__main__":
    print(smallest(1)) # 2
    print(smallest(5)) # 6
    print(smallest(123)) # 288
    print(smallest(55555)) # 663552

# Listalla on aluksi kokonaisluku 1. Joka kierroksella poistat listalta pienimmän alkion x ja 
# lisäät listalle alkiot 2x ja 3x. Mikä on listan pienin alkio n kierroksen jälkeen? Voit olettaa, että n
# on enintään 10**5.

# Esimerkiksi kun n=5, lista muuttuu näin:

# [1]→[2,3]→[3,4,6]→[4,6,6,9]→[6,6,9,8,12]→[6,9,8,12,12,18]


# Tässä tapauksessa listan pienin alkio lopussa on 6.

# Toteuta tiedostoon twothree.py funktio smallest, joka antaa vastauksen.