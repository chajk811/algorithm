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