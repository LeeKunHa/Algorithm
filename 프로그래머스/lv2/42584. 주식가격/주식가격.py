from collections import deque
def solution(prices):
    queue = deque(prices)
    answer = []
    while queue:
        v = queue.popleft()
        time = 0
        for i in queue:
            time = time+1
            if v>i:
                break
        answer.append(time)
    return answer