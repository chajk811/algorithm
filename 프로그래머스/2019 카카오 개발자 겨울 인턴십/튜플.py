def solution(s):
    result = []

    tmp = s.strip('{}')
    if '{' in tmp:
        tmp = tmp.replace('},{', ' ').split(' ')
        arr = list(map(lambda x: set(x.split(',')), tmp))
    else:
        result.append(int(tmp))
        return result

    arr.sort(key=lambda x: len(x))

    for i in range(len(arr)):
        if i == 0:
            result.append(int(list(arr[i])[0]))
        else:
            sub = arr[i] - arr[i-1]
            result.append(int(list(sub)[0]))
    
    return result