def count(t):
    counter = len(t) 
    temp = 0
    smaller = t[0] < t[1]
    for i in range(1, len(t)):
        if smaller and t[i] > t[i-1] or not smaller and t[i] < t[i-1]:
            temp += 1
        else:
            temp = 1
        counter += temp
        smaller = t[i] < t[i-1]    
    return counter

if __name__ == "__main__":
    print(count([1,2,3,4])) # 7
    print(count([1,4,2,5,3])) # 15
    print(count([7,2,1,3,5,4,6])) # 17 

# Saat syötteenä listan, jossa on jokin lukujen 1…n
# permutaatio. Tehtäväsi on laskea listan vuorottelevien osajonojen lukumäärä.

# Tässä vuorotteleva tarkoittaa sitä, että osajonossa seuraava luku on aina vuorotellen 
# pienempi tai suurempi kuin edellinen. Toisin ilmaistuna vuorotteleva osajono on sellainen, 
# joka ei sisällä ainuttakaan vähintään kolmen pituista kasvavaa eikä vähenevää osajonoa.

# Tavoitteena on, että algoritmin aikavaativuus on O(n).

# Toteuta tiedostoon alternation.py funktio count, joka palauttaa vuorottelevien osajonojen lukumäärän.