memory = {}

def count(s):
    if s in memory:
        return memory[s]
    if len(s) == 2 and s[0] == s[1]:
        return 1
    counter = 0
    for i in range(len(s)-1):
        ss = s[:i]+s[i+2:]
        if s[i] == s[i+1]:
            memory[ss] = count(ss)
            counter += memory[ss]
    return counter

if __name__ == "__main__":
    print(count("1100")) # 2
    print(count("1001")) # 1
    print(count("100111")) # 5
    print(count("11001")) # 0
    print(count("1100110011100111")) # 113925