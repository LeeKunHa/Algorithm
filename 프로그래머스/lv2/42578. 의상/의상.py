def solution(clothes):
    dic = {x[0]:x[1] for x in clothes}
    answer = 1
    for i in set(dic.values()):
        answer = answer*(list(dic.values()).count(i)+1)
    return answer-1