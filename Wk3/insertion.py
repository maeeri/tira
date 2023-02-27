from random import shuffle
import time

def insertion_sort(l):
    for i in range(len(l)):
        j = i - 1
        while j >= 0 and l[j] > l[j+1]:
            l[j], l[j+1] = l[j+1], l[j]
            j -= 1
    return l

if __name__ == "__main__":
    l = list(range(1, 10**5))
    shuffle(l)
    print(len(l))
    beginning = time.time()
    list2 = insertion_sort(l)
    end = time.time()
    print(list2 == sorted(l))
    print(end-beginning)