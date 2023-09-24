def solution(s):
    str_list = [x.capitalize() for x in s.split(' ')]
    answer = ' '.join(str_list)
    return answer