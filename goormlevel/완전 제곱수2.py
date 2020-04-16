def find(n, result):
    tmp = n ** 0.5
    if int(tmp) == tmp:
        if tmp**2 == n:
            result.append(n)
            return
    return

M, N = map(int, input().split())
result = []

for i in range(M, N+1):
    find(i, result)

print(result[0], sum(result))