def comb(arr, visit, start, tmp, cnt):
    global N, K, result

    if cnt == K:
        if tmp % N == 0:
            result += 1
        return
    
    for i in range(start, len(arr)):
        if visit[i] == 0:
            visit[i] = 1
            comb(arr, visit, i+1, tmp+arr[i], cnt+1)
            visit[i] = 0

N, K = map(int, input().split())

arr = [_ for _ in range(N)]
visit = [0 for _ in range(N)]
result = 0

comb(arr, visit, 0, 0, 0)
print(result)

## ----------------
# import itertools

# N, K = map(int, input().split())
# check = list(map(lambda x: 1 if sum(x) % N == 0 else 0, itertools.combinations([_ for _ in range(N)], K)))
# print(sum(check))