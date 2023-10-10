def solution(msg):
    answer = []
    dic = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    msg = list(msg)+['0']
    start, end = 0, 1 
    while end < len(msg):
        while ''.join(msg[start:end]) in dic:
            end += 1
        dic.append(''.join(msg[start:end]))
        answer.append(dic.index(''.join(msg[start:end-1])) + 1)
        start = end - 1
    return answer