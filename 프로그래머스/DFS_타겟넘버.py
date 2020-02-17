numbers = [1, 1, 1, 1, 1]
target = 3

def DFS(cnt, tmp, numbers, target):
    global result

    if cnt == len(numbers):
        if tmp == target:
            result += 1
        return

    DFS(cnt+1, tmp + numbers[cnt], numbers, target)
    DFS(cnt+1, tmp - numbers[cnt], numbers, target)

result = 0
DFS(0, 0, numbers, target)
print(result)
