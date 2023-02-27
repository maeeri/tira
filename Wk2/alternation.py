def count(t):
    counter = len(t) 
    temp = 0
    smaller = t[0] < t[1]
    for i in range(1, len(t)):
        if smaller and t[i] > t[i-1] or not smaller and t[i] < t[i-1]:
            temp += 1
        else:
            temp = 1
        counter += temp
        smaller = t[i] < t[i-1]    
    return counter

if __name__ == "__main__":
    print(count([1,2,3,4])) # 7
    print(count([1,4,2,5,3])) # 15
    print(count([7,2,1,3,5,4,6])) # 17 