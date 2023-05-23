def encrypt(s):
    alphabet = [*"abcdefghijklmnopqrstuvwxyz"]
    r_string = ""
    for i in range(0, len(s)):
        index = alphabet.index(s[i])
        new_index = calculate_index(index + i + 1, len(alphabet))
        r_string += alphabet[new_index]
    return r_string

        
def calculate_index(i: int, l: int):
    if i > l-1:
        return calculate_index(i-l, l)
    else:
        return i

if __name__ == "__main__":
    print(encrypt("abc")) # bdf
    print(encrypt("xz")) # yb
    print(encrypt("kkkkkkkk")) # lmnopqrs
    print(encrypt("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")) # bcdefghijklmnopqrstuvwxyzabcde

# Tehtäväsi on salata annettu merkkijono niin, että ensimmäinen merkki liikkuu aakkosissa yhden merkin eteenpäin, toinen merkki kaksi merkkiä eteenpäin, kolmas merkki kolme merkkiä eteenpäin, jne. Jos merkki kasvaa suuremmaksi kuin z, se palaa taas aakkosten alkuun.

# Merkkijono muodostuu merkeistä a–z ja siinä on enintään 100 merkkiä.

# Toteuta tiedostoon encryption.py funktio encrypt, joka tuottaa salatun merkkijonon.

# Selitys: Merkkijonossa xz merkkiä x yhtä suurempi merkki on y. Merkkiä z yhtä suurempi merkki on a, sillä z:n jälkeen siirrytään takaisin aakkosten alkuun. Merkkiä z kahta suurempi merkki on siis b. Siksi merkkijono xz salataan yb.