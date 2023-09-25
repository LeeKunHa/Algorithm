def solution(i, j, k):
    answer=0
    for num in range(i,j+1):
        for c in str(num):
            if int(c)==k:
                answer=answer+1
    return answer