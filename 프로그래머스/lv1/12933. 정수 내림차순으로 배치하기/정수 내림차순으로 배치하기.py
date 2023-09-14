def solution(n):
    answer = ''
    n = sorted(str(n), reverse=True)
    answer = ''.join(n)
    return int(answer)