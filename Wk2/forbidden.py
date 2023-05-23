def count(s, c):
    temp = ''
    counter = 0
    for i in range(0, len(s)):
        counter += len(temp)
        if s[i] == c:
            temp = ''
        else:
            temp += s[i]
    counter += len(temp)
    return counter

if __name__ == "__main__":
    print(count("abacabb", "b")) # 7
    print(count("abcdef", "g")) # 21
    print(count("xxxxxxxxx", "x")) # 0
    print(count("pupujussikainen", "u")) # 48

# Tehtäväsi on laskea, moniko merkkijonon osajono ei sisällä kiellettyä merkkiä. Syötteenä sinulle annetaan merkkijono ja merkki, jota osajonot eivät saa sisältää.

# Voit olettaa, että merkkijono muodostuu merkeistä a–z, siinä on enintään 10**5
#  merkkiä ja kielletty merkki on jokin merkeistä a–z. Tavoitteena on, että algoritmin aikavaativuus on O(n).

# Toteuta tiedostoon forbidden.py funktio count, joka palauttaa halutun tuloksen.