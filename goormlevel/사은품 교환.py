T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    
    if N == 0:
        print(0)
        continue
    elif M == 0:
        print(N//12)
    else:
        total = (N+M) // 12
        season = N // 5
        if total == season:
            print(total)
        else:
            print(min(total, season))