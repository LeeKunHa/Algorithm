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


from collections import deque
def solution(prices):
    queue = deque(prices)
    answer = []
    while queue:
        price = queue.popleft()
        sec = 0
        for q in queue:
            sec += 1
            if price > q:
                break 
        answer.append(sec)        
    return answer
