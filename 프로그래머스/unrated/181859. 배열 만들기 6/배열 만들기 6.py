def solution(arr):
    answer = []
    for i,x in enumerate(arr):
        if not answer:
            answer.append(x)
        elif answer and answer[-1]==arr[i]:
            answer.pop()
        elif answer and answer[-1]!=arr[i]:
            answer.append(x)
    if not answer:
        answer.append(-1)
    return answer