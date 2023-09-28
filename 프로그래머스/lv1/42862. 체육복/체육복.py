def solution(n, lost, reserve):
    lost, reserve = sorted([x for x in lost if x not in reserve]), sorted([x for x in reserve if x not in lost])
    answer = n - len(lost)
    for i in range(len(lost)):
        if lost[i]-1 in reserve:
            answer = answer +1
            reserve.remove(lost[i]-1)
        elif lost[i]+1 in reserve:
            answer = answer +1
            reserve.remove(lost[i]+1)
    return answer