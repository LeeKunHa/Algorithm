#방법1(리스트,for)
def solution(prices):
    answer = []
    for i in range(len(prices)):
        time = 0
        for j in prices[i+1:]:
            time = time+1
            if prices[i]>j:
                break
        answer.append(time)
    return answer

# 방법2(deque, while)
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