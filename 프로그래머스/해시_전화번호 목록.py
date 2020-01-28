def hash_func(tmp):
    length = []
    
    for l in tmp:
        if len(l) not in length:
            length.append(len(l))

    hash_table = {}
    
    for i in length:
        for j in tmp:
            if len(j) >= i:
                if not hash_table.get(j[:i]):
                    hash_table[j[:i]] = 1
                else:
                    hash_table[j[:i]] += 1
    
    return hash_table

def solution(phone_book):
    hash_table = hash_func(phone_book)
    
    for tmp in phone_book:
        if hash_table.get(tmp) > 1:
            return False
    return True