def create(n):
    l = ["A", "B", "C"]
    if n == 1:
        return l
    else:
        x = create(n-1)
        r = []
        for s in x:
            for c in l:
                r.append(s+c)
        return r


if __name__ == "__main__":
    print(create(1)) # [A,B,C]
    print(create(2)) # [AA,AB,AC,BA,BB,BC,CA,CB,CC]
    print(len(create(5))) # 243