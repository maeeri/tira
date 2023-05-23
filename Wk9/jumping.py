def rec(n, a, b, m):
    if n < a:
        return 0
    elif n == a:
        return 1
    elif n == b:
        m[n] = 1 + rec(n-a, a, b, m)
        return m[n]
    elif n in m:
        return m[n]
    else:
        for i in range(a, n+1):
            m[i] = rec(i-a, a, b, m) + rec(i-b, a, b, m)
        return m[n]

def count(n, a, b):
    memory = {}
    rec(n, a, b, memory)
    return memory[n]

if __name__ == "__main__":
    print(count(4,1,2)) # 5
    print(count(10,2,5)) # 2
    print(count(10,6,7)) # 0
    print(count(30,3,5)) # 58
    print(count(50,2,3)) # 525456
    print(count(3,1,3)) # 2

# Pelaat peliä, jossa on n tasoa. Olet aluksi tasolla 0 ja sinun tulee päästä tasolle n. 
# Joka askeleella voit hypätä a tai b tasoa ylemmäs. Monellako tavalla voit läpäistä pelin?

# Esimerkiksi kun n=4, a=1 ja b=2, tapoja on 5:
# 0→1→2→3→4
# 0→1→2→4
# 0→1→3→4
# 0→2→3→4
# 0→2→4

# Voit olettaa, että 3≤n≤50 ja 1≤a<b≤n.

# Toteuta tiedostoon jumping.py funktio count, joka ilmoittaa vastauksen.