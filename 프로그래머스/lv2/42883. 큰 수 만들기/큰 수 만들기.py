def solution(number, k):
    answer = []
    for i in range(len(number)):
        while answer and answer[-1]<number[i] and k!=0:
            answer.pop()
            k = k-1
        answer.append(number[i])
    return ''.join(answer)[:len(answer)-k]