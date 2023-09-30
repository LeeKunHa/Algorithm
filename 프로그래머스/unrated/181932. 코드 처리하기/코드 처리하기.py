def solution(code):
    mode = False
    answer = []
    for i in range(len(code)):
        if not mode:
            if code[i]=='1':
                mode = not mode
            elif code[i]!='1' and i%2==0:
                answer.append(code[i])
        elif mode:
            if code[i]=='1':
                mode = not mode
            elif code[i]!='1' and i%2==1:
                answer.append(code[i])
    if not answer:
        answer = 'EMPTY'
    else:
        answer = ''.join(answer)
    return answer