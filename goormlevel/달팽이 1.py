H, U, D, F = map(int, input().split())

day = 0
height = 0
up = U

while up > 0:
    day += 1
    height += up
    if height >= H:
        print('Success', day)
        break
    else:
        height -= D
        up -= U * F / 100
else:
    print('Failure', day+1)