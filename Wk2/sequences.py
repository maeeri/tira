def count(s):
    tira = ''
    counter = 0
    for j in range(len(s)):
        if s[j] == 't' and tira == '' or s[j] == 'i' and tira == 't' or s[j] == 'r' and tira == 'ti':
            tira += s[j]
        if s[j] == 'a' and (tira == 'tir' or tira == 'tira'):
            tira += s[j] if tira == 'tir' else ''
            counter += len(s)-j
            print(counter, len(s)-j)
    if tira == 'tira':
        arit = ''
        for j in range(len(s)-1, -1, -1):
            if s[j] == 'a' and arit == '' or s[j] == 'r' and arit == 'a' or s[j] == 'i' and arit == 'ar':
                arit += s[j]
            if s[j] == 't' and arit == 'ari':
                counter += j
                print(counter, j)
                
    return counter



    
if __name__ == "__main__":
    # print(count("ritari")) # 0
    # print(count("taikurinhattu")) # 4
    # print(count("ttiirraa")) # 4
    print(count("tixratiyra")) # 11 
    # print(count("aotiatraorirratap")) # 42