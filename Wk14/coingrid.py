def count(r):
    pass

if __name__ == "__main__":
    r =["........",
        "........",
        "...X..X.",
        "........",
        "....X...",
        "..X.X..X",
        "........",
        "....X..."]
    print(count(r)) # 3

# Annettuna on n×n -ruudukko, jonka joissain ruuduissa on kolikko.

# Yhdellä siirrolla voit kerätä kaikki kolikot haluamaltasi pysty- tai vaakariviltä. Mikä on pienin 
# tarvittava määrä siirtoja kerätä kaikki kolikot?

# Ruudukon kuvauksessa merkki . tarkoittaa tyhjää ja merkki X tarkoittaa kolikkoa. Voit olettaa, 
# että 1≤n≤20.

# Toteuta tiedostoon coingrid.py funktio count, joka ilmoittaa pienimmän määrän siirtoja kerätä 
# kaikki kolikot.