def solution(s):
    answer = 0
    s = s.split(' ')
    s.append(0)
    for i in range(len(s)-1):
        if (s[i+1] != 'Z') and (s[i] != 'Z'):
            answer = answer+int(s[i])
    return answer
