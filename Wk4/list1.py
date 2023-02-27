from time import time

l = []
begin = time()
for i in range(1, 10**5):
    l.append(i)

middle = time()
print(middle-begin)

for i in range(1, 10**5):
    l.remove(l[0])

end = time()
print(end-middle)