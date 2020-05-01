import sys

sys.stdin = open('5188_input.txt')

# 우 하
dx = [0, 1]
dy = [1, 0]

def bfs():
    Q = []
    Q.append((0, 0))
    visited[0][0] = arr[0][0]

    while Q:
        x, y = Q.pop(0)
        for d in range(2):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] == 0 or visited[nx][ny] > visited[x][y] + arr[nx][ny]:
                    Q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + arr[nx][ny]

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [[0]*N for _ in range(N)]
    bfs()

    print('#{} {}'.format(tc, visited[N-1][N-1]))