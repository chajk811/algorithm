def find(i, s, n):
    arr = []
    
    for idx in range(0, n, i):
        unit = s[idx:idx+i]
        arr.append(unit)
    
    result = []
    tmp = arr[0]
    cnt = 1
    
    for idx, unit in enumerate(arr[1:]):
        if unit == tmp:
            cnt += 1
        else:
            if cnt != 1:
                result.append(str(cnt))
            result.append(tmp)
            tmp = unit
            cnt = 1
            
        # 마지막 idx 처리 
        if idx == len(arr[1:])-1:
            if cnt != 1:
                result.append(str(cnt))
            result.append(tmp)
    
    return len(''.join(result))
    
def solution(s):
    n = len(s)
    result = n
    
    for i in range(1, int(n/2+1)):
        tmp = find(i, s, n)
        if tmp < result:
            result = tmp
    
    return result

## zip() 사용 풀이
# def compress(text, tok_len):
#     words = [text[i:i+tok_len] for i in range(0, len(text), tok_len)]
#     res = []
#     cur_word = words[0]
#     cur_cnt = 1
#     for a, b in zip(words, words[1:] + ['']):
#         if a == b:
#             cur_cnt += 1
#         else:
#             res.append([cur_word, cur_cnt])
#             cur_word = b
#             cur_cnt = 1
#     return sum(len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in res)

# def solution(text):
#     return min(compress(text, tok_len) for tok_len in list(range(1, int(len(text)/2) + 1)) + [len(text)])