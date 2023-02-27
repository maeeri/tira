from time import time
from collections import deque

l = deque()
begin = time()
for i in range(1, 10**5):
    l.append(i)

middle = time()
print(middle-begin)

for i in range(1, 10**5):
    l.popleft()

end = time()
print(end-middle)