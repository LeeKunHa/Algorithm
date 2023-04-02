def solution(array):
    answer = []
    max_ = 0
    for i in range(len(array)):
        if max_ < array[i]:
            max_ = array[i]
            answer = i
    answer = [max_,answer]
    return answer