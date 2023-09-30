def solution(s):
    change = 0
    zero = 0
    while s != '1':
        zero = zero + s.count('0')
        s = s.replace('0','')
        s = bin(len(s))[2:]
        change = change + 1
    answer = [change,zero]
    return answer