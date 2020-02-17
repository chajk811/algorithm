result = []

def find(now, num_list, visited):
    global result
    
    if len(now) > 0 and int(now):
        if int(now) not in result:
            result.append(int(now))

    for i in range(len(num_list)):
        if not visited[i]:
            tmp = now
            
            now += num_list[i]
            visited[i] = 1
            find(now, num_list, visited)
            
            now = tmp
            visited[i] = 0
            
def solution(numbers):
    global result 
    num_list = [_ for _ in numbers]
    visited = [0] * len(num_list)
    now = ''
    
    find(now, num_list, visited)
    
    cnt = 0
    for i in range(len(result)):
        if result[i] == 1:
            continue
            
        for j in range(2, result[i]):
            if result[i] % j == 0:
                break
        else:
            cnt += 1
    
    return cnt