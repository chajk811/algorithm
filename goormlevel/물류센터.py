def BFS(start, arr, N):
    visit = [0 for _ in range(N)]
    Q = []

    Q.append(start)
    visit[start] = 1

    while Q:
        now = Q.pop(0)
        for i in arr[now]:
            nxt = i[0]
            if visit[nxt] == 0:
                Q.append(nxt)
                visit[nxt] = visit[now] + i[1]

    return sum(visit) - N

N = int(input())
roads = [list(map(int, input().split())) for _ in range(N-1)]
arr = [[] for _ in range(N)]

for road in roads:
    arr[road[0]].append((road[1], road[2]))
    arr[road[1]].append((road[0], road[2]))

result = 10000

for start in range(N):
    tmp = BFS(start, arr, N)
    if tmp < result:
        result = tmp
        
print(result)