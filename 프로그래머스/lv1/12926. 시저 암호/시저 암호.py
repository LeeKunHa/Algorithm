def solution(s, n):
    answer = ''
    for i in s:
        if i.isupper():
            answer = answer+chr((ord(i)-ord('A')+n)%26+ord('A'))
        elif i.islower():
            answer = answer+chr((ord(i)-ord('a')+n)%26+ord('a'))
        else:
            answer = answer+i
    return answer