def find(s, k):
    res = []
    ss = s
    counter = 0
    while res.count("a") < k or res.count("b") < k or res.count("c") < k:
        if res.count("a") >= k and res.count("b") >= k:
            count, ss = find_closest_char(ss, "c")
            c = "c"
        elif res.count("b") >= k and res.count("c") >= k:
            count, ss = find_closest_char(ss, "a")
            c = "a"
        elif res.count("c") >= k and res.count("a") >= k:
            count, ss = find_closest_char(ss, "b")
            c = "b"
        elif res.count("a") >= k:
            count, ss, c = compare_counts(ss, "b", "c")
        elif res.count("b") >= k:
            count, ss, c = compare_counts(ss, "a", "c")
        elif res.count("c") >= k:
            count, ss, c = compare_counts(ss, "a", "b")
        else:
            count, ss, c = compare_counts(ss, "a", "b", "c")
        
        counter += count
        res.append(c)
        print(count, counter, ss, res)
    return counter
        

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