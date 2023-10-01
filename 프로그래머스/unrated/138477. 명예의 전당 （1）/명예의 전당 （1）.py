def solution(k, score):
    answer = []
    hame = []
    for i in score:
        if len(hame)<k:
            hame.append(i)
            hame.sort()
        elif hame[0]<i:
            hame.pop(0)
            hame.append(i)
            hame.sort()
        answer.append(hame[0])
    return answer