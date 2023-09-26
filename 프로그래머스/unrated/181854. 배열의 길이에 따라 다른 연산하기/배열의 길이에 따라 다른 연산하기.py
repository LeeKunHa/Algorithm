def solution(arr, n):
    answer=[]
    if len(arr)%2==1:
        for i,num in enumerate(arr):
            if i%2==0:
                num = num+n
            answer.append(num)
    else:
        for i,num in enumerate(arr):
            if i%2==1:
                num = num+n
            answer.append(num)
    return answer