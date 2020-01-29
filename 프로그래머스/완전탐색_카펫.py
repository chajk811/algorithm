def solution(brown, red):
    arr = []

    for i in range(1, red+1):
        if i in arr:
            break
        if red % i == 0:
            if red//i == i:
                arr.append(i)
            else:
                arr.append(i)
                arr.append(red // i)

    arr.sort()
    check = []

    if len(arr) % 2 != 0:
        for i in range(len(arr)//2+1):
            if i == len(arr)//2:
                check.append((arr[i], arr[i]))
            else:
                check.append((arr[i], arr[len(arr)-1-i]))
    else:
        for i in range(len(arr)//2):
            check.append((arr[i], arr[len(arr)-1-i]))

    for i in check:
        if 4 + (i[0] + i[1]) * 2 == brown:
            return [i[1]+2, i[0]+2]