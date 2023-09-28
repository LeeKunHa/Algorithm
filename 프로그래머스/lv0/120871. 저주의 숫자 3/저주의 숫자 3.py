def solution(n):
    count = [x for x in range(1,n+1) if '3' in str(x) or x%3==0]
    while len(count)!=0:
        n = n+len(count)
        count = [x for x in range(n-len(count)+1,n+1) if '3' in str(x) or x%3==0]
    answer = n
    return answer