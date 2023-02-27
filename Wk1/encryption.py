def encrypt(s):
    alphabet = [*"abcdefghijklmnopqrstuvwxyz"]
    r_string = ""
    for i in range(0, len(s)):
        index = alphabet.index(s[i])
        new_index = calculate_index(index + i + 1, len(alphabet))
        r_string += alphabet[new_index]
    return r_string

        
def calculate_index(i: int, l: int):
    if i > l-1:
        return calculate_index(i-l, l)
    else:
        return i

if __name__ == "__main__":
    print(encrypt("abc")) # bdf
    print(encrypt("xz")) # yb
    print(encrypt("kkkkkkkk")) # lmnopqrs
    print(encrypt("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")) # bcdefghijklmnopqrstuvwxyzabcde