import heapq
def solution(scoville, K):
    heap = []
    answer = 0
    for i in scoville:
        heapq.heappush(heap,i)
    while len(heap)>1 and heap[0]<K:
        lowest = heapq.heappop(heap)
        low = heapq.heappop(heap)
        heapq.heappush(heap,lowest+(low*2))
        answer = answer+1
    if heap[0] < K:
        answer = -1
    return answer