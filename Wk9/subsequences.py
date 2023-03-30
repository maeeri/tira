from random import shuffle

def f(t):
    longest = []
    for k in range(len(t)):
        longest.append(1)
        for x in range(k):
            if t[x] < t[k] and longest[x]+1 > longest[k]:
                longest[k] = longest[x]+1 
    return max(longest)

t = [i for i in range(5001)]
shuffle(t)

print(f(t))