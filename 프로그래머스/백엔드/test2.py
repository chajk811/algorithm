def solution(office, r, c, move):
    # 북, 동, 남, 서
    dy = [0, 1, 0, -1]
    dx = [-1, 0, 1, 0]
    
    N = len(office)
    now_x, now_y = r, c
    result = office[r][c]
    office[r][c] = 0
    d = 0
    
    for m in move:
        if m == 'go':
            next_x = now_x + dx[d] 
            next_y = now_y + dy[d]
            if 0 <= next_x < N and 0 <= next_y < N and office[next_x][next_y] != -1:
                now_x, now_y = next_x, next_y
                result += office[next_x][next_y]
                office[next_x][next_y] = 0
        elif m == 'left':
            d = d - 1 if d > 0 else 3
        elif m == 'right':
            d = d + 1 if d < 3 else 0
    
    return result