def solution(n):
    if n%2==1:
        answer = sum([x for x in list(range(n+1)) if x%2==1])
    else:
        answer = sum([x**2 for x in list(range(n+1)) if x%2==0])
    return answer