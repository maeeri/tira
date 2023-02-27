def count(s):
    temp = ''
    counter = 0
    for i in range(0, len(s)):
        if s[i] != s[i-1]:
            counter += sum([i for i in range(len(temp)+1)])
            temp = s[i]
        else:
            temp += s[i]
    counter += sum([i for i in range(len(temp)+1)])
    return counter
        

if __name__ == "__main__":
    print(count("aaaaa")) # 15
    print(count("abbbcaa")) # 11
    print(count("abcde")) # 5
