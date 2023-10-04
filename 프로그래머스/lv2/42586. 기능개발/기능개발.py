def solution(progresses, speeds):
    answer = []
    while progresses:
        count = 0
        while progresses and progresses[0]>=100:
            progresses.pop(0)
            speeds.pop(0)
            count = count+1
        if count>0:
            answer.append(count)
        progresses = [x+y for x,y in zip(progresses,speeds)]
    return answer


