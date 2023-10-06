def solution(N, stages):
    answer = []
    for i in range(1,N+1):
        try:
            answer.append([i, len([x for x in stages if x>i])/len([x for x in stages if x>=i])])
        except:
            answer.append([i,100])
    answer = [x[0] for x in sorted(answer,key=lambda x:x[1])]
    return answer