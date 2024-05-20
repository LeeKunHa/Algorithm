def solution(babbling):
    answer = 0
    for bab in babbling:
        for i in ['aya','ye','woo','ma']:
            if i*2 not in bab:
                bab = bab.replace(i,' ')
        if bab.isspace():
            answer = answer+1
    return answer