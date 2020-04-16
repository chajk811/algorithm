def find(n):
    global cnt
    
    tmp = n ** 0.5
    if int(tmp) == tmp:
        if tmp**2 == n:
            cnt += 1
            return
    return

N = int(input())
cnt = 0

for tc in range(N):
    n = int(input())
    find(n)

print(cnt)