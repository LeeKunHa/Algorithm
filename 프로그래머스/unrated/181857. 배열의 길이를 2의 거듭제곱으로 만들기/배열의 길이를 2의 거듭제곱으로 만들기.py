def solution(arr):
    n = 1
    while len(arr) > n:
        n = n*2
    for i in range(n-len(arr)):
        arr.append(0)
    answer = arr
    return answer