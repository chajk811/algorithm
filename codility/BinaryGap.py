def solution(N):
    tmp = bin(N)[2:].split('1')
    
    check = False
    arr = []
    
    for idx in range(len(tmp)):
        if idx == len(tmp)-1:
            if tmp[idx] != '':
                break
    
        if tmp[idx] != '': 
            arr.append(len(tmp[idx]))
    
    
    return max(arr) if len(arr) > 0 else 0