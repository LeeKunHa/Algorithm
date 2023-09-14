def solution(n):
    answer = ''
    n = sorted(list(map(int,str(n))), reverse=True)
    answer = ''.join(list(map(str,n)))
    return int(answer)