def solution(array):
    answer=0
    for i in array:
        for c in str(i):
            if int(c)==7:
                answer=answer+1
    return answer