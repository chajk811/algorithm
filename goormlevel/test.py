import sys
import itertools
# from collections import deque
# import copy
# input = sys.stdin.readline

def main():
    num = int(input())
    arr = list(map(int, input().split()))
    
    if num < 3:
        print('NO')
    elif num == 3:
        arr.sort()
        if arr[0] == arr[1] or arr[1] == arr[2]:
            print('NO')
        else:
            print('YES')
    else:
        check = list(itertools.combinations(arr, 3))
        for i in check:
            tmp = list(i)
            tmp.sort()
            if tmp[0] == tmp[1] or tmp[1] == tmp[2]:
                continue
            else:
                print('YES')
                return
        else:
            print('NO')

main()
