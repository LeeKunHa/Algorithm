def solution(n, m, section):
    answer = 0
    while section:
        answer = answer+1
        end = section[0]+m
        count = 0
        for i in section:
            if i<end:
                count = count+1
            else:
                break
        section = section[count:]
    return answer