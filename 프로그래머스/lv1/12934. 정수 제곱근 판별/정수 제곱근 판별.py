def solution(n):
    answer = -1
    for i in range(n+1):
        if n==i**2:
            answer = (i+1)**2
            break
    return answer