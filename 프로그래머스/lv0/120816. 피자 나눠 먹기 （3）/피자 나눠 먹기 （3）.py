def solution(slice, n):
    num = 1
    while slice*num < n:
        num = num+1        
    answer = num
    return answer