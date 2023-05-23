def count(s):
    dict = {}
    sq = (0, 0)
    dict[sq] = 1
    for c in s:
        m = move(c)
        sq = (sq[0] + m[0], sq[1] + m[1])
        if sq not in dict.keys():
            dict[sq] = 1
        else:
            dict[sq] += 1
    return len(dict)


def move(c):
    match c:
        case 'L':
            return (-1, 0)
        case 'R':
            return (1, 0)
        case 'U':
            return (0, -1)
        case 'D':
            return (0, 1)

if __name__ == "__main__":
    print(count("LL")) # 3
    print(count("UUDLRR")) # 5
    print(count("UDUDUDU")) # 2

# Robotti on alussa ruudussa (0,0). Tämän jälkeen robotti liikkuu annetun liikesarjan mukaisesti 
# askeleen kerrallaan. 

# Liikesarja muodostuu merkeistä U (up), D (down), L (left) ja R (right). 
# Monessako eri ruudussa robotti käy yhteensä?

# Voit olettaa, että liikesarjassa on enintään 10**5 komentoa.

# Toteuta tiedostoon robot.py funktio count, jolle annetaan robotin liikesarja ja joka ilmoittaa eri 
# ruutujen määrän.