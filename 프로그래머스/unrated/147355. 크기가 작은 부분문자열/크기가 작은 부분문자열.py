def solution(t, p):
    answer = 0
    step = 0
    for i in range(len(t)-len(p)+1):
        temp = t[step:step+len(p)]
        step = step+1
        if temp <= p:
            answer = answer+1
    return answer