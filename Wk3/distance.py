def find(t, k):
    organize(t, 0, len(t)-1)
    temp = []
    distance(t, temp)
    distance(t[1:], temp)
    temp.append(k-t[-1])
    temp.append(t[0] - 1)
    return max(temp)

def distance(t, l):
    if len(t) > 20000:
        middle = len(t) // 2
        distance(t[:middle], l)
        distance(t[middle:], l)
        l.append((t[middle+1]-t[middle])//2)
    else:
        for i in range(1, len(t)):
            l.append((t[i]-t[i-1])//2)
            
def organize(t, a, b):
    if a == b:
        return
    k = (a+b)//2
    organize(t, a, k)
    organize(t, k+1, b)
    merge(t, a, k, k+1, b)

def merge(t, a1, b1, a2, b2):
    a = a1
    b = b2
    temp = {}
    for i in range(a, b+1):
        if a2 > b2 or (a1 <= b1 and t[a1] <= t[a2]):
            temp[i] = t[a1]
            a1 += 1
        else:
            temp[i] = t[a2]
            a2 += 1
    for i in range(a, b+1):
        t[i] = temp[i]

if __name__ == "__main__":
    print(find([1, 2, 9], 11)) # 3
    print(find([2, 1, 3], 3)) # 0
    print(find([7, 4, 10, 4], 10)) # 3
    print(find([15, 2, 6, 4, 18], 20)) # 4
    print(find([41222388, 392676742, 307110407, 775934683, 25076911], 809136843)) # 191628970
    print(find([14, 15, 6, 2, 7, 14], 15)) #3
  
# Annettuna on lista kokonaislukuja, jotka kaikki ovat väliltä 1…k. 
# Listalle halutaan lisätä uusi kokonaisluku väliltä 1…k, 
# jonka etäisyys lähimpään listalla jo valmiiksi olevaan lukuun on mahdollisimman suuri. Kuinka suuri tuo etäisyys voi korkeintaan olla?

# Voit olettaa, että listalla on korkeintaan 105 lukua ja k on korkeintaan 10**9. 
# Tavoitteena on, että algoritmin aikavaativuus on O(n) tai O(nlogn).

# Toteuta tiedostoon distance.py funktio find, joka ilmoittaa suurimman mahdollisen etäisyyden.


# Selitys: Jokainen kokonaisluku väliltä 1…11 on korkeintaan 3:n päässä jostain listan [1,2,9]
# luvusta. Yksi tällainen luku on esimerkiksi 5, joka on kolmen päässä sitä lähimmästä luvusta 2. 
# Luku 6 puolestaan on kolmen päässä luvusta 9. Jokainen luku väliltä 1…3
# löytyy jo valmiiksi listalta [2,1,3]. Siksi suurin etäisyys on 0.