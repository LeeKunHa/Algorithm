import math
def solution(n):
    answer = 0
    for i in range(1,n+1):
        for j in range(2,int(math.sqrt(i))+1):
            if i%j==0:
                answer=answer-1
                break
    return answer+n-1