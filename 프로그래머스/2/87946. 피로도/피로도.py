def solution(k, dungeons):
    dungeons = sorted(dungeons, key=lambda x:x[0]-x[1], reverse=True)
    answer = 0
    while dungeons and k>0:
        clear = dungeons.pop(0)
        if k>=clear[0]:
            k = k-clear[1]
            answer = answer+1
    return answer


from itertools import permutations
def solution(k, dungeons):
    dungeons = list(permutations(dungeons,len(dungeons)))
    answer = 0
    for i in dungeons:
        count = 0
        k_ = k
        for j in i:
            if k_>=j[0]:
                k_ = k_-j[1]
                count = count+1
            else:
                break
        answer = max(answer,count)
    return answer

