def solution(n,a,b):
    answer = 1
    while abs(a-b)>=1:
        a = (a//2)+(a%2)
        b = (b//2)+(b%2)
        answer = answer+1
    return answer-1