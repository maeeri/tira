def eval(s):
    a = s.split(' ')
    temp = []
    operations = []
    indices = []
    res = 0
    for i in range(len(a)):
        if a[i] in ['(+', '(*', '(/', '(-']:
            operations.append(a[i][1])
            indices.append(i)
            if i > 0:
                temp.append(' '.join(a[indices[-2]:i]))
        if a[i][-1] == ')' and len(indices) > 0:
            end_b = a[i].count(')')-1
            index = indices.pop()
            op = operations.pop()
            l = []
            for y in range(index+1, i+1):
                l.append(get_int(a[y]))
            temp.append(str(count(op, l)) + ')' * end_b)
            if len(a[i+1:]) > 0:
                temp.append(' '.join(a[i+1:]))
            return eval(' '.join(temp))
    return get_int(s)

def get_int(s):
    return int(s[:-s.count(')')]) if s[-1] == ')' else int(s)


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
    print(eval("(+ 1 2 3 4 5)")) # 15
    print(eval("(+ 5 (* 3 2) 7)")) # 18
    print(eval("(* (+ (+ 1 2) 3) (+ (* 4 5) 6 2))")) # 168
    print(eval("(+ 123 456)")) # 579
    print(eval("(+ 7 4 (* 5 8 0 (* 6 1)) (+ 1 9 (* 6 7)))")) # 63