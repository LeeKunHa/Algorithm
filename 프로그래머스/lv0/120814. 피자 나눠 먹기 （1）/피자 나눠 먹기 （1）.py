def solution(n):
    answer = 1
    while(answer*7/n < 1):
        answer = answer+1
    return answer