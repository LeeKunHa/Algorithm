def solution(n):
    answer = 0
    for i in range(1,n//2+1):
        start = i
        end = i+1
        sum_ = start
        while sum_<=n:
            if sum_ == n:
                answer = answer+1
            sum_ = sum_+end
            end = end+1
    return answer+1