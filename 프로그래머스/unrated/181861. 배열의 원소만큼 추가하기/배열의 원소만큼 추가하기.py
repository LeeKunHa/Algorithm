def solution(arr):
    answer =[]
    for i in arr:
        single = [i]*i
        answer = answer+single
    return answer