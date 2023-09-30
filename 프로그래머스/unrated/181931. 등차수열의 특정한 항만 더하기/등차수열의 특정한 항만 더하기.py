def solution(a, d, included):
    answer = []
    for i,x in enumerate(included):
        if x==True:
            answer.append(a+(d*i))
    answer = sum(answer)
    return answer