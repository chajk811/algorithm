# 1
def solution(p,s):
    result = 0
    
    for idx in range(len(p)):
        now = int(p[idx])
        target = int(s[idx])
        
        if now < target:
            cnt1 = abs(now - target)
            cnt2 = now + (9 - target) + 1
        elif now > target:
            cnt1 = abs(now - target)
            cnt2 = (9 - now) + target + 1
        
        result += min(cnt1, cnt2) if not now == target else 0
    
    return result

# 2
def solution(office, r, c, move):
    # 북, 동, 남, 서
    dy = [0, 1, 0, -1]
    dx = [-1, 0, 1, 0]
    
    N = len(office)
    now_x, now_y = r, c
    result = office[r][c]
    office[r][c] = 0
    d = 0
    
    for m in move:
        if m == 'go':
            next_x = now_x + dx[d] 
            next_y = now_y + dy[d]
            if 0 <= next_x < N and 0 <= next_y < N and office[next_x][next_y] != -1:
                now_x, now_y = next_x, next_y
                result += office[next_x][next_y]
                office[next_x][next_y] = 0
        elif m == 'left':
            d = d - 1 if d > 0 else 3
        elif m == 'right':
            d = d + 1 if d < 3 else 0
    
    return result

# 3
import copy

MIN = 0xfffff

def find(numbers, arr, K, visited, cnt):
    global MIN

    # 종료 조건 1
    if cnt >= MIN:
        return

    # 확인하는 부분
    tmp = arr[1:] + [arr[0]]
    for a, b in zip(arr, tmp):
        if abs(a - b) > K:
            break
    else:
        if MIN > cnt:
            MIN = cnt
            return
    
    # 종료 조건 2
    if 0 not in visited:
        return

    # 재귀 부분
    for i in range(len(numbers)-1):
        if visited[i] == 0:
            now, next_num = arr[i], arr[i+1]
            arr[i] = next_num
            arr[i+1] = now
            visited[i] = 1
            
            cnt += 1
            find(numbers, arr, K, visited, cnt)
            arr[i], arr[i+1] = now, next_num
            cnt -= 1
            visited[i] = 0
            
def solution(numbers, K):
    global MIN
    
    visited = [0] * len(numbers)
    arr = copy.deepcopy(numbers)
    cnt = 0

    find(numbers, arr, K, visited, cnt)
    
    return MIN