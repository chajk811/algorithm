def perm(arr, visit, cnt, n, tmp):
    if cnt == n:
        print(visit)
        print(tmp)
        print('-----')
        return

    for i in range(0, len(arr)):
        if visit[i] == 0:
            visit[i] = 1
            tmp.append(arr[i])
            perm(arr, visit, cnt+1, n, tmp)
            visit[i] = 0
            tmp.remove(arr[i])


# 3P2
arr = [_ for _ in range(3)]
visit = [0 for _ in range(3)]
perm(arr, visit, 0, 2, [])
