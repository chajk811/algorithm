def divide(Str):
    num1, num2 = 0, 0 # num1 : '(', num2 : ')'
    u, v = '', ''
    cnt = 0

    while cnt < len(Str):
        if Str[cnt] == '(':
            num1 += 1
        elif Str[cnt] == ')':
            num2 += 1

        if num1 == num2:
            u = Str[:cnt+1]
            v = Str[cnt+1:]
            return u, v
        cnt += 1


# check는 u에만 수행함으로, u의 길이는 0이상이다.
def check(tmp):
    Stack = []
    Stack.append(tmp[0])
    cnt = 0

    while cnt+1 < len(tmp):
        if Stack:
            now = Stack[-1]
            if now == '(' and tmp[cnt+1] == ')':
                Stack.pop()
            else:
                Stack.append(tmp[cnt+1])
        else:
            Stack.append(tmp[cnt+1])
        cnt += 1

    if Stack:
        return False
    else:
        return True

def solution(Str):
    u, v = divide(Str)
    result = ''

    if check(u):
        tmp = solution(v) if v else ''
        return u + tmp
    else:
        tmp = solution(v) if v else ''
        result = '(' + tmp + ')'
        if len(u) > 2:
            u = list(u[1:len(u)-1])
            for idx in range(len(u)):
                if u[idx] == '(':
                    u[idx] = ')'
                elif u[idx] == ')':
                    u[idx] = '('
            u = ''.join(u)
        else:
            u = ''
        result += u

    return result
