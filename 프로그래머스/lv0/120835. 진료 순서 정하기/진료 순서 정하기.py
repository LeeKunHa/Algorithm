def solution(emergency):
    answer = []
    for i in range(len(emergency)):
        step = 0
        while len(emergency) > step:
            if emergency[i] == sorted(emergency, reverse=True)[step]:
                answer.append(step+1)
                break
            step = step+1
    return answer