def solution(d, budget):
    answer = 0
    d.sort()
    while d!=[] and budget >= d[0]:
        answer = answer+1
        budget = budget - d.pop(0)
    return answer