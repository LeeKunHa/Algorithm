from collections import deque
def solution(priorities, location):
    priorities_deque = deque([[i,x] for i,x in enumerate(priorities)])
    answer = 0
    while priorities_deque:
        while priorities_deque[0][1] != max([x[1] for x in priorities_deque]):
            priorities_deque.rotate(-1)
        v = priorities_deque.popleft()
        if v[0] == location:
            return answer+1
        answer = answer+1