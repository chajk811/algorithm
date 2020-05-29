import heapq

nums = [4, 1, 7, 3, 8, 5]
heap = []

# max heap 구현
# 튜플 형식으로 넣어주기 (우선 순위, 값)
# 큰 값의 음수를 취하면 가장 작은 값이 되므로
# (-값, 값) 형태로 heappush() 해주기

for num in nums:
    heapq.heappush(heap, (-num, num)) # (우선 순위, 값)

print(heap)

while heap:
    print(heapq.heappop(heap)[1])