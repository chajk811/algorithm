# 1
def solution(purchase):
    cal = []

    # 달력 생성
    for i in range(1, 8):
        if i % 2 == 0:
            if i == 2:
                cal.append([0]*28)
            else:
                cal.append([0]*30)
        else:
            cal.append([0]*31)

    for i in range(8, 13):
        if i % 2 != 0:
            cal.append([0]*30)
        else:
            cal.append([0]*31)

    # 금액 입력
    for p in range(len(purchase)):
        tmp = purchase[p].split(' ')
        date = [int(tmp[0][5]+tmp[0][6]),int(tmp[0][8]+tmp[0][9])]
        money = int(tmp[1])

        cnt = 30
        sm, sd = date[0]-1, date[1]-1
        while cnt > 0:
            if sd < len(cal[sm]):
                cal[sm][sd] += money
            else:
                sm += 1
                sd = 0
                cal[sm][sd] += money
            sd += 1
            cnt -= 1

    # 등급 확인
    result = [0] * 5
    for c in range(len(cal)):
        for cc in range(len(cal[c])):
            if 0 <= cal[c][cc] < 10000:
                result[0] += 1
            elif 10000 <= cal[c][cc] < 20000:
                result[1] += 1
            elif 20000 <= cal[c][cc] < 50000:
                result[2] += 1
            elif 50000 <= cal[c][cc] < 100000:
                result[3] += 1
            else:
                result[4] += 1

    return result

# 2
def solution(ip_addrs, langs, scores):
    hash_table = {}
    N = len(ip_addrs)
    langs = list(map(lambda x: 'C' if x[0] == 'C' else x, langs))

    for tmp in range(N):
        if ip_addrs[tmp] not in hash_table:
            hash_table[ip_addrs[tmp]] = [tmp]
        else:
            hash_table[ip_addrs[tmp]].append(tmp)

    result = 0
    for value in hash_table.values():
        # 4명 이상일때
        if len(value) >= 4:
            result += len(value)
        # 3명일때
        elif len(value) == 3:
            s1, s2, s3 = value[0], value[1], value[2]
            if langs[s1] == langs[s2] and langs[s1] == langs[s3]:
                result += 3
        # 2명일때
        elif len(value) == 2:
            s1, s2 = value[0], value[1]
            if langs[s1] == langs[s2]:
                if scores[s1] == scores[s2]:
                    result += 2
    return N - result

# 3
def change(new_id):
    S, N = '', ''
    for char in new_id:
        if char.isalpha():
            S += char
        else:
            N += char
    n = int(N) + 1 if N else 1

    return S + str(n)

def solution(registered_list, new_id):
    arr = registered_list
    new = new_id

    while new in arr:
        new = change(new)
    else:
        return new

# 4
def solution(macaron):
    return ["000000" for _ in range(6)]