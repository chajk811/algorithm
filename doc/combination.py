def comb(arr, visit, start, cnt, n):
    if cnt == n:
        print(visit)
        return
    
    for i in range(cnt, len(arr)):
        if visit[i] == 0:
            visit[i] = 1
            comb(arr, visit, i+1, cnt +1, n)
            visit[i] = 0

arr = [_ for _ in range(3)]
visit = [0 for _ in range(3)]
comb(arr, visit, 0, 0, 2)


# def combination(arr, r):
#     arr = sorted(arr)

#     def generate(chosen):
#         if len(chosen) == r:
#             print(chosen)
#             return

#         start = arr.index(chosen[-1]) + 1 if chosen else 0
#         # print(start)
#         for nxt in range(start, len(arr)):
#             chosen.append(arr[nxt])
#             generate(chosen)
#             chosen.pop()
    
#     generate([])

# combination([0, 1, 2, 3, 4], 3)