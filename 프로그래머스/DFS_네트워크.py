def dfs(start, visited, n, computers):
    S = []
    S.append(start)
    
    while S:
        now = S.pop()
        visited[now] = 1
        
        for i in range(n):
            if computers[now][i] == 1 and visited[i] == 0:
                S.append(i)
                
        
def solution(n, computers):
    visited = [0 for _ in range(n)]
    cnt = 0
    
    for i in range(n):
        if visited[i] == 0:
            dfs(i, visited, n, computers)
            cnt += 1
    
    return cnt

# def dfs(graph, start_node):
#     visit = list()
#     stack = list()
    
#     stack.append(start_node)
    
#     while stack:
#         node = stack.pop()
#         if node not in visit:
#             visit.append(node)
#             stack.extend(graph[node])
    
#     return visit
    
# def solution(n, computers):
#     graph = {node: [] for node in range(n)}
    
#     for i, computer in enumerate(computers):
#         for j, conn in enumerate(computer):
#             if i != j and conn == 1:
#                 graph[i].append(j)
    
#     paths = map(sorted, [dfs(graph, node) for node in graph])
    
#     return len(set(["".join(map(str, path)) for path in paths]))