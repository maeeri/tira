
def get_ss(t, k, longest):
    if k in longest:
        return longest[k]
    else:
        for x in range(k):
            if k not in longest: longest[k] = 1
            if abs(t[x]-t[k]) <= 1 and longest[x]+1 > longest[k]:
                longest[k] = longest[x]+1

def find(t):
    longest = {0:1}
    for k in range(len(t)):
        get_ss(t, k, longest)
    m = 1
    for k in longest:
        if longest[k] > m:
            m = longest[k]
    return m

if __name__ == "__main__":
    print(find([1,2,3,4,5])) # 5
    print(find([5,5,5,5,5])) # 5
    print(find([5,2,3,8,2,4,1])) # 4
    print(find([1,3,5,7,9])) # 1
    print(find([4, 1, 7, 4, 7, 6, 9, 8, 8, 4])) # 4

# Tehtäväsi on etsiä listasta pisin alijono, jossa jokaisen kahden vierekkäisen luvun ero on enintään 1. 
# Esimerkiksi listassa [5,2,3,8,2,4,1] pisin tällainen alijono on [2,3,2,1], jonka pituus on 4.

# Voit olettaa, että 1≤n≤100 ja jokainen listan alkio on kokonaisluku välillä 1≤n≤100.

# Toteuta tiedostoon onediff.py funktio find, joka antaa pisimmän alijonon pituuden.