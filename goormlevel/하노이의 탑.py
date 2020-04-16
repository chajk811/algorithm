def find(n, a, b, c):
    if n == 1:
        result.append([a, c])
    else:
        find(n-1, a, c, b)
        result.append([a, c])
        find(n-1, b, a, c)

N = int(input())
result = []

find(N, 1, 2, 3)

print(len(result))