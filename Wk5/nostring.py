def find(s):
    a = [*s]
    if len(set(a)) < 26:
        return 1
    for i in range(2, len(s)//2):
        temp = []
        for j in range(len(s)-i+1):
            temp.append(s[j:j+i])
        if len(set(temp)) < 26**i:
            return i

if __name__ == "__main__":
    print(find("zzz")) # 1
    print(find("aybabtu")) # 1
    print(find("abcdefghijklmnopqrstuvwxyz")) # 2