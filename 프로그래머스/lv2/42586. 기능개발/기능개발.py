from collections import deque
def solution(progresses, speeds):
    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)
    while progresses:
        progresses = deque([x+j for x,j in zip(progresses,speeds)])
        if progresses[0] >= 100:
            count = 0
            while progresses and progresses[0] >= 100:
                progresses.popleft()
                speeds.popleft()
                count = count+1
            answer.append(count)
    return answer