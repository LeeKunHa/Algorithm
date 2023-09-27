def solution(before, after):
    if sorted(list(before))==sorted(list(after)):
        answer = 1
    else:
        answer = 0
    return answer