import time
from random import randint

def hidas(merkit):
    laskuri = 0
    for i in range(0, len(merkit)):
        for j in range(i + 1, len(merkit)):
            if merkit[i] == 0 and merkit[j] == 1:
                laskuri +=1
    print(laskuri)

def nopea(merkit):
    laskuri = 0
    nollat = 0
    for i in range(0, len(merkit)):
        if merkit[i] == 0:
            nollat += 1
        else:
            laskuri += nollat
    print(laskuri)


if __name__ == "__main__":
    merkit = list(randint(0,1) for i in range(0, 100000))
    
    alku = time.time()
    nopea(merkit)
    loppu = time.time()
    print("aikaa kului", loppu-alku, "s")

    alku = time.time()
    hidas(merkit)
    loppu = time.time()
    print("aikaa kului", loppu-alku, "s")