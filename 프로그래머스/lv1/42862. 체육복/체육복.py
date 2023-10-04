def solution(n, lost, reserve):
    lost, reserve = sorted([x for x in lost if x not in reserve]), sorted([x for x in reserve if x not in lost])
    answer = n - len(lost)
    for i in lost:
        if i-1 in reserve:
            reserve.remove(i-1)
            answer = answer+1
        elif i+1 in reserve:
            reserve.remove(i+1)
            answer = answer+1
    return answer



