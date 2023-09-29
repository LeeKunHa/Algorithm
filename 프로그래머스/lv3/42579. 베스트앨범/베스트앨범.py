def solution(genres, plays):
    dic = {}
    for i in set(genres):
        dic[i]=0
    for i,j in zip(genres,plays):
        dic[i] = dic[i]+j
    alb = sorted([[i,j,k] for i,j,k in zip(genres,plays,range(len(plays)))], key=lambda x:(dic[x[0]],x[1]),reverse=True)
    
    answer = []
    count = 0
    before = 'temp'
    for i,j,k in alb:
        if i == before:
            count = count+1
        else:
            count = 1
        if count < 3:
            answer.append(k)
        before = i
    return answer
    