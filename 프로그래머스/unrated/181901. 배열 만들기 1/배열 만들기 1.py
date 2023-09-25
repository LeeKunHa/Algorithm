def solution(n, k):
    answer = sorted([x for x in list(range(1,n+1)) if x%k==0])
    return answer