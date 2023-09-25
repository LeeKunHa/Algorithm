def solution(num, total):
    answer = []
    max = total//num+num//2
    for i in range(max-num+1,max+1):
        answer.append(i)
    return answer