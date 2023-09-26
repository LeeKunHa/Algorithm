def solution(arr, intervals):
    answer = sum([arr[x[0]:x[1]+1] for x in intervals],[])
    return answer