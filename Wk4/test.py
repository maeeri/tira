def solve(s):
    i = 0
    temp = ''
    while True:
        temp, i = loop(s, i, temp)
        if i >= len(s) - 1: break
    if s == temp:
        return temp
    else:
        return solve(temp)

def loop(s, i, temp):
    r = compare_chars(s[i], s[i+1]) if i < len(s)-1 else s[i]
    temp += r if i == len(s)-2 else r[0]
    if r[0] == s[i]:
        i += 1
    else:
        i += 2
    if i < len(s) and r == s[i]:
        loop(s, i, temp)
    return temp, i


def compare_chars(c1, c2):
    if c1 == c2:
        return 'a' if c1 == 'z' else chr(ord(c1)+1)
    else: return c1 + c2

if __name__ == "__main__":
    print(solve("auto")) # auto
    print(solve("ddqqirr")) # eris
    print(solve("aaaaaa")) # cb
    print(solve("wsstuva")) # xa
    print(solve("zzzzzzzz")) # c
    print(solve("mlkjihgfedcbb")) # n
    print(solve("kkkjjiikjkjiikjjiijkjji")) # mjkjmlki
    # s = 'a' * 10**5
    # print(solve(s))