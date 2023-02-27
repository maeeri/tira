def count(s, k):
    dict = {}
    sq = (0, 0)
    dict[sq] = 1
    additions_per_round = {}
    for i in range(len(s)*4):
        l = len(dict)
        for c in s:
            m = move(c)
            sq = (sq[0] + m[0], sq[1] + m[1])
            if sq not in dict.keys():
                dict[sq] = 1
            else:
                dict[sq] += 1
        additions_per_round[i] = len(dict) - l
    if len(dict) == len(s)**2*4+1: return k*len(s) + 1
    elif len(dict) == len(s): return len(dict)
    else: 
        return 1 + sum(list(additions_per_round.values())[:len(s)]) + (k-len(s)) * additions_per_round[len(s)]

def move(c):
    match c:
        case 'L':
            return (-1, 0)
        case 'R':
            return (1, 0)
        case 'U':
            return (0, -1)
        case 'D':
            return (0, 1)
        
if __name__ == "__main__":
    print(count("UR", 100)) # 201
    print(count("UD", 100)) # 2
    print(count("UURRDDL", 500)) # 1506
    print(count("L", 10**9)) # 1000000001
    print(count("DLUR", 10**9)) # 4
    print(count("UURRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRDDLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL", 1000000000)) # 3000000144