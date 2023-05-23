#ei toimi vielä

def count(s):
    indices = {'t': [], 'i': [], 'r': [], 'a': []}
    counter = 0
    for j in range(len(s)):
        match s[j]:
            case 't':
                indices['t'].append(j)
            case 'i':
                if len(indices['t']) > 0:
                    indices['i'].append(j)                
            case 'r':
                if len(indices['i']) > 0:
                    indices['r'].append(j)
            case 'a':
                if len(indices['r']) > 0:
                    indices['a'].append(j)
    tira = []
    for x in range(len(indices['a'])-1, -1, -1):
        temp = [indices['a'][x]]

        for y in range(len(indices['r'])-1, -1, -1):
            if indices['r'][y] < indices['a'][x]:
                temp.append(indices['r'][y])
                break
        if len(temp) < 2: continue
        for y in range(len(indices['i'])-1, -1, -1):
            if indices['i'][y] < temp[-1]:
                temp.append(indices['i'][y])
                break
        if len(temp) < 3: continue
        for y in range(len(indices['t'])-1, -1, -1):
            if indices['t'][y] < temp[-1]:
                temp.append(indices['t'][y])
                break
        if len(temp) < 4: continue
        tira.append(temp)

    t = list(set([x[3] for x in tira]))
    a = list(set([x[0] for x in tira]))
    print(t, a)
    print(len(s))
    if len(a) > 0 and len(t) > 0:
        counter += len(s) - min(a)
        counter += max(t)

    return counter




    
if __name__ == "__main__":
    print(count("ritari")) # 0
    print(count("taikurinhattu")) # 4
    print(count("ttiirraa")) # 4
    print(count("tixratiyra")) # 11 
    print(count("aotiatraorirratap")) # 42


# Tehtäväsi on laskea, moniko annetun merkkijonon osajono sisältää merkkijonon tira alijonona.

# Merkkijono sisältää jonon tira alijonona silloin, kun merkkijonosta voidaan muodostaa merkkijono 
# tira poistamalla siitä mahdollisesti osa merkeistä muuttamatta merkkien järjestystä. 
# Esimerkiksi taikurinhattu sisältää sanan tira alijonona, mutta ritari ei sisällä.

# Voit olettaa, että merkkijono muodostuu merkeistä a–z ja siinä on enintään 10**5
# merkkiä. Tavoitteena on, että algoritmin aikavaativuus on O(n).

# Toteuta tiedostoon sequences.py funktio count, joka palauttaa sellaisten osajonojen määrän, 
# joilla on tira alijonona.