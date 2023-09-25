def solution(str_list, ex):
    answer = ''.join([x for x in str_list if ex not in x])
    return answer