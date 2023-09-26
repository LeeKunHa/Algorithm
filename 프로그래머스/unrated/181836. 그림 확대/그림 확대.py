def solution(picture, k):
    answer = []
    for i in picture:
        temp = ''
        for j in i:
            temp = temp+j*k
        for num in range(k):
            answer.append(temp)
    return answer