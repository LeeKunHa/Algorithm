import heapq
def solution(n, works):
    heap = []
    for i in works:
        heapq.heappush(heap,-i)
    for i in range(n):
        max_ = -heapq.heappop(heap)
        heapq.heappush(heap,-max_+1)

    heap = [-x for x in heap]
    if sum(heap)<=0:
        answer = 0
    else:
        answer = sum([x**2 for x in heap])
    return answer