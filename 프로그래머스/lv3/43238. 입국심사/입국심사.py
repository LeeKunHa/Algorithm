def solution(n, times):
    left = 1
    right = max(times)*n
    while left<right:
        mid = (left+right)//2
        total = 0
        for i in times:
            total = total + mid//i
        if total<n:
            left = mid+1
        else:
            right = mid
    answer = left
    return answer