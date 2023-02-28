def count(s):
    indices = {'t': [], 'i': [], 'r': [], 'a': []}
    counter = 0
    for i in range(len(s)):
        if s[i] in ['t', 'i', 'r', 'a']:
            indices[s[i]].append(i)
    print(indices)

    return counter




    
if __name__ == "__main__":
    print(count("ritari")) # 0
    print(count("taikurinhattu")) # 4
    print(count("ttiirraa")) # 4
    print(count("tixratiyra")) # 11 
    print(count("aotiatraorirratap")) # 42