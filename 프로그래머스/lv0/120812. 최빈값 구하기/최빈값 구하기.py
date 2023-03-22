def solution(array):
    frequency = []
    for i in range(1000):
        frequency.append(0)
    for i in array:
        frequency[i] = frequency[i]+1
    
    max_ = 0
    num = 0
    for i in frequency:
        if i > max_:
            max_ = i
            answer = num
        elif i == max_:
            answer = -1
        num = num+1
    return answer