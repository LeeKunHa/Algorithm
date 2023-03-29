def solution(n):
    answer = []
    while n>=2:
        for i in range(2,n+1):
            if n%i == 0:
                n = int(n/i)
                answer.append(i)
                break
    return sorted(set(answer))