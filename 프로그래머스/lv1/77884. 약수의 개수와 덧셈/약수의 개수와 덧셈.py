def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        count = 0
        for j in range(1,i):
            if i%j == 0:
                count = count+1
        if count%2==1:
            answer = answer+i
        else:
            answer = answer-i
    return answer