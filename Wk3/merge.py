from random import shuffle
import time

def merge_sort(l):
    organize(0, len(l)-1)

def organize(a, b):
    if a == b:
        return
    k = (a+b)//2
    organize(a, k)
    organize(k+1, b)
    combine(a, k, k+1, b)

def combine(a1, b1, a2, b2):
    a = a1
    b = b2
    temp = {}
    for i in range(a, b+1):
        if a2 > b2 or (a1 <= b1 and l[a1] <= l[a2]):
            temp[i] = l[a1]
            a1 += 1
        else:
            temp[i] = l[a2]
            a2 += 1
    for i in range(a, b+1):
        l[i] = temp[i]

if __name__ == "__main__":
    l = list(range(1, 10**5))
    shuffle(l)
    beginning = time.time()
    merge_sort(l)
    end = time.time()
    print(l == sorted(l))
    print(end-beginning)