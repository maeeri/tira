memory = {}

def count(s):
    if s == "":
        return 0
    if s in memory:
        return memory[s] + 1
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                memory[s[:i]+s[j+1:]] = count(s[:i]+s[j+1:])
    return memory[s]

if __name__ == "__main__":
    print(count("1100")) # 2
    print(count("1001")) # 1
    # print(count("100111")) # 5
    # print(count("11001")) # 0
    # print(count("1100110011100111")) # 113925