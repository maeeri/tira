def create(n):
    a = []
    create_array(1, n, a)
    return a

def get_middle(b, e):
    if (b+(e-b))%2==0:
        return b + (e-b)//2
    return b + (e-b)//2

def create_array(b, e, a):
    m = get_middle(b, e)
    a.append(m)
    if e-m == 1: a.append(e)
    elif e-m > 1: create_array(m+1, e, a)
    if m-b == 1: a.append(b)
    elif m-b > 1: create_array(b, m-1, a)
    

if __name__ == "__main__":
    print(create(1)) # [1]
    print(create(3)) # [2, 3, 1]
    print(create(4)) # [2, 1, 4, 3]
    print(create(7)) # [4, 6, 5, 2, 3, 7, 1]