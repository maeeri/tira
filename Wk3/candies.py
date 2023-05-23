def solve(prices, x):
    t = sorted(prices)
    sum = 0
    items = 0
    for i in range(0, len(t)):
        sum += t[i]
        items += 1
        if sum == x:
            return items
        if sum > x:
            return items - 1
    return items

if __name__ == "__main__":
    print(solve([1, 1, 1, 1], 2)) # 2
    print(solve([2, 5, 3, 2, 8, 7], 10)) # 3
    print(solve([2, 3, 4, 5], 1)) # 0
    print(solve([2, 3, 4, 5], 10**9)) # 4
    print(solve([10**9, 1, 10**9], 10**6)) # 1

# Kaupassa on myytävänä n
#  karkkia, joilla jokaisella on tietty hinta. Montako karkkia voit ostaa enintään, kun sinulla on rahaa x?

# Karkkien määrä on enintään 10**5, ja jokaisen karkin hinta ja x
#  on välillä 1…10**9. Tavoitteena on, että algoritmin aikavaativuus on O(n)
#  tai O(nlogn).

# Toteuta tiedostoon candies.py funktio solve, joka ilmoittaa, montako karkkia voit ostaa enintään.

# Selitys: Ensimmäisessä esimerkissä voit ostaa mitkä tahansa kaksi karkkia. Toisessa esimerkissä voit ostaa kolme karkkia, 
# esimerkiksi listan kolme ensimmäistä karkkia, jotka maksavat yhteensä 10. 
# Kolmannessa esimerkissä et voi ostaa mitään karkkia, koska jokainen maksaa enemmän kuin 1.