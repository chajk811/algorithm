import heapq

# k 번째 작은 값
def kth_min(nums, k):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)

    tmp = None
    for _ in range(k):
        tmp = heapq.heappop(heap)
    
    return tmp

# k 번째 큰 값
def kth_max(nums, k):
    heap = []
    for num in nums:
        heapq.heappush(heap, (-num, num))

    tmp = None
    for _ in range(k):
        tmp = heapq.heappop(heap)
    
    return tmp[1]

arr = [4, 1, 7, 3, 8, 5]
print(sorted(arr))
print(kth_min(arr, 3))
print(kth_max(arr, 3))