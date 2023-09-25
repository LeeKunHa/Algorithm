def solution(array, n):
    answer = array[0]
    for i in array[1:]:
        if abs(n-i)<abs(n-answer):
            answer = i
        elif abs(n-i)==abs(n-answer):
            answer = min(i,answer)
    return answer