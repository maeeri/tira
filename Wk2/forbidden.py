def count(s, c):
    temp = ''
    counter = 0
    for i in range(0, len(s)):
        counter += len(temp)
        if s[i] == c:
            temp = ''
        else:
            temp += s[i]
    counter += len(temp)
    return counter

if __name__ == "__main__":
    print(count("abacabb", "b")) # 7
    print(count("abcdef", "g")) # 21
    print(count("xxxxxxxxx", "x")) # 0
    print(count("pupujussikainen", "u")) # 48
