from collections import Counter
def solution(n):
    answer = n+1
    while True:
        if Counter(bin(answer)[2:])['1'] == Counter(bin(n)[2:])['1']:
            break
        answer = answer+1
    return answer
