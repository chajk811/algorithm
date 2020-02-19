def find(start, N, K):
    dx = [-(K-1), K-1]
    visit = [0 for _ in range(N)]
    cnt = 0
    stack = []
    check = [False, False]
    
    stack.append(start)
    visit[start] = 1

    while stack:
        x = stack.pop()
        visit[x] = 1
        for d in range(2):
            nx = x + dx[d]
            if 0 <= nx < N and visit[nx] == 0:
                stack.append(nx)
                cnt += 1
    
    if visit[0] == 1:
        check[0] = True
    if visit[N-1] == 1:
        check[1] = True

    return cnt, check


N, K = map(int, input().split())
arr = list(map(int, input().split()))

min_idx = arr.index(1)
result = N

for i in range(K):
    if 0 <= min_idx-i < N:
        tmp, check = find(min_idx-i, N, K)
        tmp += check.count(False)
        if tmp < result:
            result = tmp

print(result)