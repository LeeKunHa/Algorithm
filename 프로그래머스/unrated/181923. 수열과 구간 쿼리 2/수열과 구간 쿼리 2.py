def solution(arr, queries):
    answer = []
    for s,e,k in queries:
        over_k = [x for x in arr[s:e+1] if x>k]
        if over_k:
            answer.append(min(over_k))
        else:
            answer.append(-1)
    answer = answer
    return answer