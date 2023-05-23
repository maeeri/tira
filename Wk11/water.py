def count(a,b,x):
    pass

if __name__ == "__main__":
    print(count(5,4,2)) # 22
    print(count(4,3,2)) # 16
    print(count(3,3,1)) # -1
    print(count(10,9,8)) # 46
    print(count(123,456,42)) # 10530

# Sinulla on vesiastiat, joiden tilavuudet ovat a ja b litraa, ja tavoitteesi on mitata x litraa vettä astioiden avulla.

# Astiat ovat aluksi tyhjiä, eikä niissä ole mitta-asteikkoa. Joka askeleella saat täyttää tai tyhjentää jommankumman astian tai kaataa vettä astioiden välillä. Kuitenkin joka askeleella ainakin toisen astioista on täytyttävä tai tyhjennyttävä kokonaan, koska muuten mittaus ei olisi tarkka.

# Mikä on pienin mahdollinen siirrettävän veden kokonaismäärä, jolla saat mitattua x litraa vettä 
# ensimmäiseen astiaan? Esimerkiksi kun a=5, b=4 ja x=2, pienin siirtomäärä on 22 litraa. 
# Tässä on yksi optimaalinen ratkaisu:

# 1. Täytä ensimmäinen astia (vettä siirtyy 5 litraa)
# 2. Kaada ensimmäisestä astiasta toinen astia täyteen (vettä siirtyy 4 litraa)
# 3. Tyhjennä toinen astia (vettä siirtyy 4 litraa)
# 4. Kaada ensimmäisen astian sisältö toiseen astiaan (vettä siirtyy 1 litraa)
# 5. Täytä ensimmäinen astia (vettä siirtyy 5 litraa)
# 6. Kaada ensimmäisestä astiasta toinen astia täyteen (vettä siirtyy 3 litraa)
# 7. Voit olettaa, että 1≤a,b≤500 ja 1≤x≤a. Jos mitään ratkaisua ei ole olemassa, haluttu vastaus on −1.

# Toteuta tiedostoon water.py funktio count, joka kertoo pienimmän mahdollisen siirrettävän veden kokonaismäärän.