def solution(s):
    p,y = 0,0
    for i in s:
        if i.lower() == 'p':
            p = p+1
        elif i.lower() == 'y':
            y = y+1
    answer = p==y
    return answer