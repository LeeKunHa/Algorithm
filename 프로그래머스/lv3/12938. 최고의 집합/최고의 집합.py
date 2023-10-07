def solution(n, s):
    answer = [s//n]*(n)
    for i in range((s%n)):
        answer[i]=answer[i]+1
    answer.sort()
    if answer[0] == 0:
        answer = [-1]
    return sorted(answer)