def bfs(begin, target, words, visited):
    Q = []
    Q.append(begin)
    
    while Q:
        now = Q.pop(0)
        if now == target:
            return
        
        for word in words:
            tmp = list(now)
            for w in list(word):
                if w in tmp:
                    tmp.remove(w)
                
            if len(tmp) == 1 and visited[words.index(word)] == 0:
                Q.append(word)
                if now == begin:
                    visited[words.index(word)] = 1
                else:
                    visited[words.index(word)] = visited[words.index(now)] + 1

                        
def solution(begin, target, words):
    visited = [0 for _ in range(len(words))]
    
    if target not in words:
        return 0
    
    bfs(begin, target, words, visited)

    return visited[words.index(target)]