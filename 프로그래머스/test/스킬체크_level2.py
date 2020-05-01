# 1 - 1
def solution(arr1, arr2):
    answer = []
    for idx1 in range(len(arr1)):
        row = []
        for idx2 in range(len(arr2[0])):
            tmp = 0
            for idx3 in range(len(arr1[0])):
                tmp += arr1[idx1][idx3] * arr2[idx3][idx2]
            row.append(tmp)
        answer.append(row)
    return answer

# 1 - 2
def solution(arr1, arr2):
    a = len(arr1)
    b = len(arr1[0])
    c = lne(arr2[0])

    return [[sum([arr1[idx1][idx3] * arr2[idx3][idx2] for idx3 in range(B)]) for idx2 in range(C)] for idx1 in range(A)]

# 1 - 3
def productMatrix(A, B):
return [[sum(a*b for a, b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]
# zip(*arr) 2차원 배열인 arr를 열로 묶어줌.
# zip(arr1, arr2) 두 개의 list의 인덱스가 같은 각각의 요소끼리 계산이 필요할 때 유용함.

# 2
def solution(A,B):
    result = 0

    A.sort()
    B.sort(reverse=True)

    for i in range(len(A)):
        tmp = A[i] * B[i]
        result += tmp

    return result