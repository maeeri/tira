from random import shuffle

def create(n):
    n_list = list(i for i in range(n, 0, -1))
    return n_list
        

if __name__ == "__main__":
    print(create(6)) # [3, 1, 6, 2, 4, 5]
    print(create(10)) # [7, 10, 3, 1, 5, 4, 8, 6, 9, 2]
    print(create(1005)) # [9, 4, 6, 14, 15, 13, 12, 11, 5, 2, 3, 8, 1, 7, 10]