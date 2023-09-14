def solution(n, m):
    for i in range(n,0,-1):
        if n%i==0 and m%i==0:
            max_ = i
            break
    for i in range(m,m*n+1):
        if i%n==0 and i%m==0:
            min_ = i
            break
    answer = [max_,min_]
    return answer