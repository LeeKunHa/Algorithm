from collections import deque
def solution(priorities, location):
    queue = deque(enumerate(priorities))
    answer = 0
    while queue:
        while queue and queue[0][1] != max([x[1] for x in queue]):
            queue.rotate(-1)
        v = queue.popleft()
        if v[0] == location:
            return answer+1
        answer = answer+1
