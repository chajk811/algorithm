import copy

# key 를 90도 회전시키기
def rotate(key):
    rotate_key = copy.deepcopy(key)

    y = len(key) - 1
    for i in range(len(key)):
        x = 0
        for j in range(len(key)):
            rotate_key[x][y] = key[i][j]
            x = x + 1
        y = y - 1
    
    return rotate_key


# 자물쇠 숫자 2로 padding 하기
def padding(key, lock):
    len_key = len(key)
    len_lock = len(lock)

    # 왼쪽 오른쪽 padding
    for i in range(len_lock):
        lock[i] = [2]*(len_key-1) + lock[i] + [2]*(len_key-1)
    
    # 윗부분 아랫부분 padding
    for _ in range(len_key-1):
        lock.insert(0, [2]*((len_key-1)*2 + len_lock))
        lock.append([2]*((len_key-1)*2 + len_lock))

    # lock을 padding 시켜주는 것이 목적이므로, return 값 X


def solution(key, lock):
    # 열쇠
    key = key
    key_90 = rotate(key)
    key_180 = rotate(key_90)
    key_270 = rotate(key_180)

    # 자물쇠
    lock = lock

    # 자물쇠 '0'의 갯수
    lock_0 = 0
    for i in range(len(lock)):
        lock_0 += lock[i].count(0)

    padding(key, lock)
    answer = False

    for x in range(len(lock)-len(key)+1):
        for y in range(len(lock)-len(key)+1):
            cnt = 0
            for i in range(len(key)):
                for j in range(len(key)):
                    if lock[x+i][y+j] == 0:
                        cnt += 1
            if cnt == lock_0:
                for tmp in [key, key_90, key_180, key_270]:
                    cnt_tmp = cnt
                    check = False
                    for k in range(len(key)):
                        if check:
                            break
                        for l in range(len(key)):
                            if lock[x+k][y+l] == 2:
                                continue
                            elif lock[x+k][y+l] == 1 and tmp[k][l] == 1:
                                check = True
                                break
                            elif lock[x+k][y+l] == 0 and tmp[k][l] == 1:
                                cnt_tmp -= 1
                    if cnt_tmp == 0:
                        answer = True
                        return answer
    return answer