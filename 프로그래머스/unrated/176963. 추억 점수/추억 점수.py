def solution(name, yearning, photo):
    dic = {x:y for x,y in zip(name,yearning)}
    answer = []
    for i in photo:
        answer.append(sum([dic[x] for x in i if x in dic.keys()]))
    return answer