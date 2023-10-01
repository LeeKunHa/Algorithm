def solution(k, m, score):
    answer = 0
    score = sorted(score, reverse=True)[:len(score)//m*m]
    for i in range((len(score)//m)):
        answer = answer + min(score[i*m:i*m+m])*len(score[i*m:i*m+m])
    return answer