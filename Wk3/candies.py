def solve(prices, x):
    t = sorted(prices)
    sum = 0
    items = 0
    for i in range(0, len(t)):
        sum += t[i]
        items += 1
        if sum == x:
            return items
        if sum > x:
            return items - 1
    return items

if __name__ == "__main__":
    print(solve([1, 1, 1, 1], 2)) # 2
    print(solve([2, 5, 3, 2, 8, 7], 10)) # 3
    print(solve([2, 3, 4, 5], 1)) # 0
    print(solve([2, 3, 4, 5], 10**9)) # 4
    print(solve([10**9, 1, 10**9], 10**6)) # 1