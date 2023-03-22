def solution(num_list):
    m = 0
    s = 0
    for i in num_list:
        if i%2 == 0:
            m = m+1
        elif i%2 != 0:
            s = s+1
    answer = [m,s]
    return answer