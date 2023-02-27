from collections import deque

def solve(n,k):
    l = deque(range(1,n+1))
    for i in range(k):
        a = l.popleft()
        b = l.popleft()
        l.append(b)
        l.append(a)
    return l[0]

if __name__ == "__main__":
    print(solve(4,3)) # 4
    print(solve(12,5)) # 11
    print(solve(99,555)) # 11
    print(solve(12345,54321)) # 9875