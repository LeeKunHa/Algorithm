import heapq
def solution(operations):
    heap = []
    for i in operations:
        if heap and i == 'D 1':
            heap.remove(max(heap))
        elif heap and i == 'D -1':
            heapq.heappop(heap)
        elif i[0] == 'I':
            heapq.heappush(heap,int(i[2:]))
    if heap:
        answer = [max(heap),min(heap)]
    else:
        answer = [0,0]
    return answer