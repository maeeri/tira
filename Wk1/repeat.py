def find(s):
    for i in range(len(s)):
        substring = s[:i+1]
        test = substring * (len(s)//len(substring))
        if test == s:
            return len(substring)

if __name__ == "__main__":
    print(find("aaa")) # 1
    print(find("abcd")) # 4
    print(find("abcabcabcabc")) # 3
    print(find("aybabtuaybabtu")) # 7
    print(find("abcabca")) # 7

# Tehtäväsi on selvittää, kuinka pitkä on lyhin merkkijono, jota toistamalla voidaan muodostaa annettu merkkijono. 
# Esimerkiksi kun merkkijono on abcabcabcabc, lyhin toistettava merkkijono on abc.

# Merkkijono muodostuu merkeistä a–z ja siinä on enintään 100 merkkiä.

# Toteuta tiedostoon repeat.py funktio find, joka antaa toistettavan merkkijonon pituuden.