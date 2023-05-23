def generate(n):
    seq = [11]
    t = 0
    while t < n:
        for i in range(seq[t], seq[t]+100):
            if check_for_same_digit(i) and i not in seq:
                seq.append(i)
        t += 1
    return seq[n-1]

def check_for_same_digit(n):
    sep = [*str(n)]
    for d in sep:
        if sep.count(d) > 1: return True
    return False

if __name__ == "__main__":
    print(generate(1)) # 11
    print(generate(2)) # 22
    print(generate(3)) # 33
    print(generate(10)) # 100
    print(generate(123)) # 505

# Lukujonon jokainen alkio on pienin positiivinen kokonaisluku, jota ei ole vielä esiintynyt lukujonossa ja jossa on yksi tai useampi toistuva numero.

# Lukujono alkaa näin:

# 11,22,33,44,55,66,77,88,99,100,101,110,111,112,113,114,…


# Tehtäväsi on etsiä lukujonon kohdassa n
#  oleva luku. Voit olettaa, että n
#  on enintään 1000
# .

# Toteuta tiedostoon sequence.py funktio generate, joka palauttaa halutun lukujonon alkion.