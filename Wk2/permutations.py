def count(a, b):
    d_a = {}
    d_b = {}
    for i in range(len(a)):
        d_a[a[i]] = i
        d_b[b[i]] = i
    return len([i for i in d_a if d_a[i] < d_b[i]])

if __name__ == "__main__":
    print(count([1,2,3], [1,2,3])) # 0
    print(count([2,3,4,1], [1,2,3,4])) # 3
    print(count([4,7,3,1,6,2,5], [5,6,1,2,4,3,7])) # 3
    print(count([5,4,9,1,8,3,2,6,7], [6,2,8,4,9,1,5,7,3])) # 5

# Sinulle annetaan kaksi listaa A ja B, 
# joissa molemmissa on lukujen 1…n
# jokin permutaatio (eli molemmat listat sisältävät luvut 1…n
# jossain järjestyksessä).

# Tehtäväsi on laskea, moniko luvuista 1…n
#  esiintyy aiemmin listalla A
#  kuin listalla B. 
# Tavoitteena on, että algoritmin aikavaativuus on O(n).

# Toteuta tiedostoon permutations.py funktio count, joka palauttaa halutun tuloksen.