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


def solution(genres, plays):
    answer = []
    dic = {x:0 for x in genres}
    for i,j in zip(genres,plays):
        dic[i] = dic[i]+j
    alb = [[i,y,x] for i,x,y in zip(range(len(plays)),genres,plays)]
    alb = sorted([x for x in alb], key=lambda x:(dic[x[2]],x[1]), reverse=True)
    
    answer.append(alb[0][0])
    gen = alb[0][2]
    count = 1
    for i in alb[1:]:
        if i[2]==gen:
            count = count+1
        else:
            gen = i[2]
            count = 1
        if count>2:
            pass
        else:
            answer.append(i[0])
    return answer
    
    
    
    