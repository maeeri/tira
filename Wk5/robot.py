def count(s):
    dict = {}
    sq = (0, 0)
    dict[sq] = 1
    for c in s:
        m = move(c)
        sq = (sq[0] + m[0], sq[1] + m[1])
        if sq not in dict.keys():
            dict[sq] = 1
        else:
            dict[sq] += 1
    return len(dict)


def move(c):
    match c:
        case 'L':
            return (-1, 0)
        case 'R':
            return (1, 0)
        case 'U':
            return (0, -1)
        case 'D':
            return (0, 1)

if __name__ == "__main__":
    print(count("LL")) # 3
    print(count("UUDLRR")) # 5
    print(count("UDUDUDU")) # 2