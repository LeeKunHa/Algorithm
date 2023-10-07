def solution(n, times):
    start = 1
    end = max(times)*n
    while start<end:
        mid = (start+end)//2
        total = 0
        for i in times:
            total = total + mid//i
        if total<n:
            start = mid+1
        else:
            end = mid
    answer = start
    return answer