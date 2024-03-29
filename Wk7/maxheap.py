from math import floor, log2

def count(n):
    counter = 0
    full_lvls = floor(log2(n))
    nodes_per_lvl = [2**i for i in range(full_lvls + 1)]
    on_last_lvl = nodes_per_lvl[-1] - sum(nodes_per_lvl)%n
    
    for i in range(full_lvls):
        counter += i * nodes_per_lvl[i]

    counter += full_lvls * on_last_lvl
    return counter


if __name__ == "__main__":
    print(count(4)) # 4
    print(count(7)) # 10
    print(count(10)) # 19
    print(count(123)) # 618
    print(count(999999999)) # 27926258178

# Maksimikekoon lisätään järjestyksessä luvut 1,2,…,n. Kuinka monta kertaa kahden eri alkion 
# paikkaa vaihdetaan keskenään keossa kyseisen prosessin aikana? Voit olettaa, että n on korkeintaan 10**9.

# Esimerkiksi kun n=4, vaihdot ovat järjestyksessä 1↔2, 2↔3, 1↔4 ja 3↔4, joten vastaus on 4.

# Toteuta tiedostoon maxheap.py fuktio count, joka antaa vaihtojen määrän.