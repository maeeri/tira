def count(a, b):
    pass

if __name__ == "__main__":
    print(count("AAA", "BBB")) # 0
    print(count("AB", "BA")) # 1
    print(count("AA", "AA")) # 3
    print(count("ABA", "BAB")) # 2
    print(count("AAABBB", "BBBAAA")) # 3
    print(count("AABABBBA", "BAABABAB")) # 13

# Annettuna on kaksi samanpituista merkkijonoa, jotka molemmat koostuvat merkeistä A ja B. 
# Tehtäväsi on laskea, moniko ensimmäisen merkkijonon osajono on toisen merkkijonon samassa 
# kohdassa olevan osajonon anagrammi.

# Kaiksi merkkijonoa ovat toistensa anagrammeja, 
# jos niissä on jokaista merkkiä yhtä monta. Voit olettaa, että merkkijonojen pituudet on enintään 10**5.

