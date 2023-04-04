def solution(my_str, n):
    answer = []
    for i in range(int(len(my_str)/n)+1):
        if my_str[:n] != '':
            answer.append(my_str[:n])
            my_str = my_str[n:]
    return answer