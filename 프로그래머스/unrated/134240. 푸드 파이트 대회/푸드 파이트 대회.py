def solution(food):
    answer = ''
    for i,x in enumerate(food):
        answer = answer+str(i)*(x//2)
    answer = answer+'0'+answer[::-1]
    return answer