def solution(s):
    answer = ''
    s = s.split(' ')
    for i in s:
        for j in range(len(i)):
            if j%2 == 0:
                answer = answer+(i[j].upper())
            else:
                answer = answer+i[j].lower()
        answer = answer+' '
    return answer[:-1]