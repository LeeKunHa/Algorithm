def solution(order):
    answer = 0
    for i in order:
        if 'cafelatte' in i:
            answer=answer+5000
        else:
            answer=answer+4500
    return answer