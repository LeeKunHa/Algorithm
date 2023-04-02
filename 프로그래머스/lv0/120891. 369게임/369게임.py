def solution(order):
    answer = 0
    for i in str(order):
        if i in '369':
            answer = answer+1
    return answer