from time import time
from random import randint

# def hash(s: str):
#     a = 19
#     n = 10**6
#     h = 0
#     for i in range(len(s)):
#         h += a**(len(s)-i-1) * ord(s[i])

#     print(h%n)


arr = []
for i in range(0, 10**6):
    arr.append(randint(1,10**9))

beginning = time()

sorted_arr = sorted(arr)
different = 1

for i in range(len(sorted_arr)-1):
    if sorted_arr[i] != sorted_arr[i+1]:
        different += 1

middle = time()

print(middle - beginning)

arr_set = {}
for a in arr:
    if a not in arr_set.keys():
        arr_set[a] = 1
    else: arr_set[a] += 1

end = time()

print(different)
print(len(arr_set))
for a in arr_set.values():
    if a > 1: print(a)

print(end-middle)