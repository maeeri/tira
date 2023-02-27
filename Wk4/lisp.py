def eval(s):
    a = s.split(' ')
    temp = []
    operation = ''
    open = 0
    res = 0
    i = 0
    for i in range(len(a)):
        if a[i][0] == '(':
            operation = a[i][1]
            for j in range(i+1, len(a)):
                if a[j][0] == '(':
                    open += a[j].count('(')
                    temp.append(eval(' '.join(a[j:])))
                elif a[j][-1] == ')':
                    temp.append(int(a[j].replace(')', '')))
                    open -= a[j].count(')')
                    res += count(operation, temp)
                    i = j
                    break
                else:
                    temp.append(int(a[j]))
        elif a[i][-1] == ')':
            temp.append(int(a[j].replace(')', '')))
            open -= a[j].count(')')
            res += count(operation, temp)
            temp.clear()
        else:
            # temp.append(int(a[i]))
            pass
    return res


def count(s, l):
    r = 0
    match s:
        case '+':
            for n in l: r += n
        case '*':
            r = 1
            for n in l: r *= n
        case '-':
            r = l[0]
            for i in range(1, len(l)): r -= l[i]
        case '/':
            r = r[0]
            for i in range(1, len(l)): r /= l[i]
    return int(r)
            

if __name__ == "__main__":
    # print(eval("(+ 1 2 3 4 5)")) # 15
    print(eval("(+ 5 (* 3 2) 7)")) # 18
    # print(eval("(* (+ (+ 1 2) 3) (+ (* 4 5) 6 2))")) # 168
    # print(eval("(+ 123 456)")) # 579