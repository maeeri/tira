def count_minimum_height_trees(n):
    if n == 0 or n == 1:
        return 1
    if n == 2:
        return 2
    count = 0
    for i in range(n//2):
        count += count_minimum_height_trees(i) * count_minimum_height_trees(n-i-1)
    if n % 2 == 0:
        count += count_minimum_height_trees(n//2-1) * count_minimum_height_trees(n//2)
    return count



print(count_minimum_height_trees(7))