def solution(clothes):
    table = {}
    
    for tmp in clothes:
        if not table.get(tmp[1]):
            table[tmp[1]] = 1
        else:
            table[tmp[1]] += 1
    
    total = 1
    
    for i in table.values():
        total *= i + 1
    
    return total-1