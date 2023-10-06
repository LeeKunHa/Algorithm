def solution(N, stages):
    answer = []
    for i in range(1,N+1):
        total = stages.count(i)
        if total==0:
            fail = 0
        else:
            fail = total/len([x for x in stages if x>=i])
        answer.append([i,fail])
    answer = [x[0] for x in sorted(answer, key=lambda x:x[1], reverse=True)]
    return answer