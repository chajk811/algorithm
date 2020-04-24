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