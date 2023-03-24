def solution(numbers, k):
    num = ((k-1)*2)%len(numbers)
    answer = numbers[num]
    return answer


