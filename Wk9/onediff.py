subseq = {}

def do_something(t, o):
    for k in range(len(t)):
        pass


def find(t):
    if t == []:
        return 0
    if str(t) in subseq:
        return subseq[t]
    for i in range(len(t)):
        temp = []
        temp.append(t[i])
        for j in range(1, len(t)):
            for l in range(len(temp)-1, -1, -1):
                if abs(t[j]-temp[l]) <= 1:
                    temp.append(t[j])
                    subseq[str(temp)] = len(temp)
    print(subseq)

if __name__ == "__main__":
    # print(find([1,2,3,4,5])) # 5
    # print(find([5,5,5,5,5])) # 5
    # print(find([5,2,3,8,2,4,1])) # 4
    # print(find([1,3,5,7,9])) # 1
    print(find([4, 1, 7, 4, 7, 6, 9, 8, 8, 4])) # 4