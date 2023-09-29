def solution(clothes):
    dic = dict([])
    for i in clothes:
        dic[i[0]] = i[1]
    answer = 1
    for i in list(set(dic.values())):
        answer = answer * (list(dic.values()).count(i)+1)
    return answer-1