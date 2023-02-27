def generate(n):
    seq = [11]
    t = 0
    while t < n:
        for i in range(seq[t], seq[t]+100):
            if check_for_same_digit(i) and i not in seq:
                seq.append(i)
        t += 1
    return seq[n-1]

def check_for_same_digit(n):
    sep = [*str(n)]
    for d in sep:
        if sep.count(d) > 1: return True
    return False

if __name__ == "__main__":
    print(generate(1)) # 11
    print(generate(2)) # 22
    print(generate(3)) # 33
    print(generate(10)) # 100
    print(generate(123)) # 505