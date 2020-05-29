import heapq

heap = []

heapq.heappush(heap, 4)
heapq.heappush(heap, 1)
heapq.heappush(heap, 7)
heapq.heappush(heap, 3)
heapq.heappush(heap, 5)
heapq.heappush(heap, 4)

print(heap)

print(heapq.heappop(heap))
print(heap)
# 가장 작은 값이 인덱스 0에 위치
# 인덱스 0을 pop 한다.
# 그렇다고 인덱스 1과 인덱스 2가 그 다음으로 작은 수가 아닐 수 있으므로,
# 최소 값을 찾으려면 heappop()을 사용해서 확인하자.

heap = [2, 5, 6, 8, 1]
heapq.heapify(heap)
print(heap)