def find(s, k):
    a, b, c = 0, 0, 0
    i_b, i_e = 0, len(s)//2
    beginning, end = s[:len(s)//2], s[len(s)//2:]

    r = 0
    while True:
        a, b, c = get_char(s[i_b], a, b, c)
        r += 1
        if check_all(a, b, c, k):
            break
        else:
            a, b, c = get_char(s[i_e], a, b, c)
            r += 1
        if check_all(a, b, c, k):
            break
        i_b += 1
        i_e -= 1
    return r

def get_char(ch, a, b, c):
    match(ch):
        case 'a':
            a += 1
        case 'b':
            b += 1
        case 'c':
            c += 1    
    return a, b, c

def check_all(a, b, c, k):
    return check_condition(a, k) and check_condition(b, k) and check_condition(c, k)

def check_condition(v, k):
    return v >= k

def find_closest_char(string, char):
    i_b = string.find(char)
    i_e = string.rfind(char)
    if (len(string) - i_e) <= i_b:
        return (len(string) - i_e, string[:i_e])
    else:
        return (i_b +1, string[i_b+1:])
    
def compare_counts(string, char1, char2, char3=""):
    count1, ss1 = find_closest_char(string, char1)
    count2, ss2 = find_closest_char(string, char2)
    if char3 != "": 
        count3, ss3 = find_closest_char(string, char3)
        result = (count1, ss1, char1) if count1 < count2 and count1 < count3 else (count2, ss2, char2) if count2 < count1 and count2 < count3 else (count3, ss3, char3)
    else:
        result = (count1, ss1, char1) if count1 < count2 else (count2, ss2, char2)
    return result

if __name__ == "__main__":
    print(find("abc", 1)) # 3
    print(find("aabca", 1)) # 3
    print(find("aaaabbbcccc", 1)) # 6
    print(find("aabbaacc", 2)) # 6
    print(find("aaaabbbbaaaccccaaccacbbaa", 3)) # 13