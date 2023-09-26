def solution(arr):
    answer = 0
    match = []
    while match!=arr:
        match = arr.copy()
        for i,x in enumerate(arr):
            if x >= 50 and x%2==0:
                arr[i] = arr[i]/2
            elif x < 50 and x%2==1:
                arr[i] = arr[i]*2+1
        answer = answer+1
    return answer-1