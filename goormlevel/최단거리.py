N = int(input())
arr = list(map(int, input().split()))
d = [0 for _ in range(N-1)]

for i in range(N-1):
    d[i] = arr[i+1] - arr[i]

print(min(d))
