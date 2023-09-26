def solution(arr, flag):
    answer = ''
    for i,x in enumerate(arr):
        if flag[i]==True:
            answer=answer+str(arr[i])*arr[i]*2
        else:
            answer=answer[:-arr[i]]
    return list(map(int,answer))