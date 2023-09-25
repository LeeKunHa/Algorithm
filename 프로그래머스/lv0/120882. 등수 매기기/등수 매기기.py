def solution(score):
    answer = []
    average = sorted([sum(x)/2 for x in score],reverse=True)
    for i in score:
        answer.append(average.index(sum(i)/2)+1)
    return answer