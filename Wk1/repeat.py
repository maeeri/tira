def find(s):
    for i in range(len(s)):
        substring = s[:i+1]
        test = substring * (len(s)//len(substring))
        if test == s:
            return len(substring)

if __name__ == "__main__":
    print(find("aaa")) # 1
    print(find("abcd")) # 4
    print(find("abcabcabcabc")) # 3
    print(find("aybabtuaybabtu")) # 7
    print(find("abcabca")) # 7