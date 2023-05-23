memory = {}

def count(s):
    if s in memory:
        return memory[s]
    if len(s) == 2 and s[0] == s[1]:
        return 1
    counter = 0
    for i in range(len(s)-1):
        ss = s[:i]+s[i+2:]
        if s[i] == s[i+1]:
            memory[ss] = count(ss)
            counter += memory[ss]
    return counter

if __name__ == "__main__":
    print(count("1100")) # 2
    print(count("1001")) # 1
    print(count("100111")) # 5
    print(count("11001")) # 0
    print(count("1100110011100111")) # 113925

# Annettuna on bittijono, jossa on n merkkiä. Joka askeleella saat poistaa kaksi vierekkäistä bittiä, jotka ovat samat. Monellako tavalla voit poistaa kaikki bitit?

# Esimerkiksi kun bittijono on 100111, mahdollisia tapoja on 5:
# - 100−−111→11−−11→11−−→ (tyhjä)
# - 100−−111→111−−1→11−−→ (tyhjä)
# - 100−−111→1111−−→11−−→ (tyhjä)
# - 10011−−1→100−−1→11−−→ (tyhjä)
# - 100111−−→100−−1→11−−→ (tyhjä)

# Voit olettaa, että 1≤n≤30.

# Toteuta tiedostoon biterase.py funktio count, joka kertoo, monellako tapaa voit poistaa kaikki bitit.