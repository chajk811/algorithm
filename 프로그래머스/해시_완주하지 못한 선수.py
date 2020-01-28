def hash_func(tmp_list):
    hash_table = {}
    
    for i in tmp_list:
        if i not in hash_table:
            hash_table[i] = 1
        else:
            hash_table[i] += 1
    
    return hash_table
    
def solution(participant, completion):
    hash_table = hash_func(completion)
    
    for i in participant:
        if not hash_table.get(i):
            return i    
        else:
            hash_table[i] -= 1