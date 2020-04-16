# 코니와 브라운의 위치 p : 0 <= x <= 200,000
# 코니 1초 후 1만큼 움직이고, 매 초 +1 만큼해서 움직인다.
# 브라운 현재 위치 B - 1, B + 1, B * 2 중 하나로 움직인다.
# 브라운은 범위를 벗어나는 위치로는 이동할 수 없고, 코니가 범위를 벗어나면 게임 끝.

from collections import deque
C, B = map(int, input().split())

time = 1
result = 0
current_C = C
dq = deque([B])
found = False

while True:
    if current_C > 200000:
        answer = -1
        break

    current_C += time
    for _ in range(len(dq)):
        num = dq.popleft()
        b_plus = num + 1
        b_minus = num - 1 
        b_times = num * 2

        if b_plus == current_C or b_minus == current_C or b_times == current_C:
            answer = time
            found = True
            break
        else:
            dq.append(b_plus)
            dq.append(b_minus)
            dq.append(b_times)
    
    if found:
        break
    
    time += 1

print(answer)