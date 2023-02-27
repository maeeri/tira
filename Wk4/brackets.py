def balance(s):
    o = 0
    br = []
    stack = []
    ast = s.count('*')
    ob = s.count('(')
    cb = s.count(')')
    if ast > 0: 
        last = s.rindex('*')
        ob = s[last:].count('(')
        cb = s[last:].count(')') - ob
    for i in range(len(s)):
        match s[i]:
            case '(':
                stack.append('(')
                o += 1
                pass
            case '*':
                if i == last:
                    if o-cb < 1: return None
                    br.append(o-cb)
                    for j in range(o-cb):
                        stack.append(')')
                        b = check_stack(stack)
                    o -= o-cb
                else:
                    stack.append(')')
                    br.append(1)
                    b = check_stack(stack)
                    o -= 1
            case ')':
                stack.append(')')
                check_stack(stack)
                o -= 1
    if len(stack) > 0:
        return None           
    return br

def check_stack(stack):
    if len(stack) >= 2 and stack[-2] == '(' and stack[-1] == ')':
        stack.pop()
        stack.pop()
        return True
    return False

if __name__ == "__main__":
    print(balance("*(")) # None
    print(balance("(*")) # [1]
    print(balance("(())")) # []
    print(balance("(((((*")) # [5]
    print(balance("(((((*(")) # None
    print(balance("((((*(()*()*")) # [2,2,1]
    print(balance("((*))(((*")) # None
    print(balance("(((()**(**")) # [1,1,1,1]
    print(balance("(((**()")) # [1,2]
    print(balance("(()(***"))
