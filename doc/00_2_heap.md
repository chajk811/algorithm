## heap

출처 : https://www.daleseo.com/python-heapq/

### `heapq(힙큐)` 

이진 트리(binary tree) 기반의 최소 힙(min heap) 자료구조를 제공합니다.

min heap을 사용하면 원소들이 항상 정렬된 상태로 추가/삭제되며, min heap에서 가장 작은값은 언제나 인덱스 0, 즉, 이진 트리의 루투에 위치합니다.

내부적으로 min heap 내의 모든 원소(k)는 항상 자식 원소들 (2k+1, 2k+2) 보다 크기가 작거나 같도록 원소가 추가되고 삭제됩니다.



```python
# 모듈 임포트
import heapq

# 최소 힙 생성
# heapq 모듈은 파이썬의 보통 리스트를 마치 최소 힙처럼 다룰 수 있도록 도와준다.
heap = []

# 힙에 원소 추가
# heappush() 함수를 사용하여 힙에 원소를 추가한다.
# 첫번째 인자는 원소를 추가할 대상 리스트이며, 두번째 인자는 추가할 원소를 넘깁니다.
heapq.heappush(heap, 4)
heapq.heappush(heap, 1)
heapq.heappush(heap, 7)
heapq.heappush(heap, 3)
print(heap)
# => [1, 3, 7, 4]
# 가장 작은 1이 인덱스 0에 위치하며, 인덱스 1(=k)에 위차한 3은 인덱스
# 3(2k+1)에 위치한 4보다 크므로 힙의 공식을 만족합니다.
# 내부적으로 이진 트리에 원소를 추가하는 heappush() 함수는 0(logN)의 시간복잡도를 가진다.

# 힙에서 원소 삭제
# heappop() 함수를 이용하여 힙에서 원소를 삭제할 수 있다.
# 원소를 삭제할 대상 리스트를 인자로 넘기면, 가장 작은 원소를 삭제 후에 그 값을 리턴한다.
print(heapq.heappop(heap))
print(heap)
# => 1
# => [3, 4, 7]

# 최소값 삭제하지 않고 얻기
# 힙에서 최소값을 삭제하지 않고 단순히 읽기만 하려면 일반적으로 리스트의 첫번째 원소에 접근하듯이 인덱스를 통해서 접근하면 된다.
print(heap[0])
# => 3
# 여기서 주의사항은 인덱스 0에 가장작은 원소가 있다고 해서, 인덱스 1에 두번째 작은 원소, 인덱스 2에 세번째 작은 원소가 있다는 보장은 없다는 것이다. 왜냐하면 힙은 heappop() 함수를 호출하여 원소를 삭제할 때마다 이진 트리의 재배치를 통해 매번 새로운 최소값을 인덱스 0에 위치시키기 때문이다. 따라서 두번째로 작은 원소를 얻으려면 바로 heap[1]으로 접근하면 안되고, 반드시 heappop()을 통해 가장 작은 원소를 삭제 후에 heap[0]을 통해 새로운 최소값에 접근해야 한다.

# 기존 리스트를 힙으로 변환
heap = [4, 1, 7, 3, 8, 5]
heapq.heapify(heap)
print(heap)
# => [1, 3, 5, 4, 8, 7]
```



### (응용) 최대 힙

`heapq` 모듈은 최소 힙(min heap)은 기능만을 동작하기 때문에 최대 힙(max heap)으로 활용하려면 약간의 요령이 필요하다.

바로 힙에 튜플(tuple)를 원소로 추가하거나 삭제하면, 튜플 내에서 맨 앞에 있는 값을 기준으로 최소 힙이 구성되는 원리를 이용하는 것이다.

따라서, 최대 힙을 만들려면 각 값에 대한 우선 순위르 구한 후, (우선 순위, 값) 구조의 튜플(tuple)을 힘에 추가하거나 삭제하면 된다.

그리고 힙에서 값을 읽어올 때는 각 튜플에서 인덱스 1에 있는 값을 취하면 된다.

```python
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

```



### (응용) K번째 최소값/최대값

최소 힙이나 최대 힙을 사용하면 K번째 최소값이나 최대값을 효율적으로 구할 수 있다.

```python
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
```



### (응용) 힙 정렬

힙 정렬(heap sort)은 위에서 설명드린 힙 자료구조의 성질을 이용한 대표적인 정렬 알고리즘입니다.

```python
import heapq

def heap_sort(nums):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
    
    sorted_nums = []
    while heap:
        sorted_nums.append(heapq.heappop(heap))
    
    return sorted_nums

arr =  [4, 1, 7, 3, 8, 5]
print(heap_sort(arr))
```



