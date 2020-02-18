def bfs(begin, target, words, visited):
    Q = []
    Q.append(begin)
    
    while Q:
        now = Q.pop(0)
        print(now, visited)
        
        for word in words:
            tmp = set(list(now)) - set(list(word))
            if len(tmp) == 1:
                if visited[words.index(word)] == 0 or visited[words.index(word)] > visited[words.index(now)]:
                    Q.append(word)
                    if now == begin:
                        visited[words.index(word)] = 1
                    else:
                        visited[words.index(word)] = visited[words.index(now)] + 1
    
    return visited
    
def solution(begin, target, words):
    visited = [0 for _ in range(len(words))]
    
    if target not in words:
        return 0
    
    bfs(begin, target, words, visited)
    
    return visited[words.index(target)]