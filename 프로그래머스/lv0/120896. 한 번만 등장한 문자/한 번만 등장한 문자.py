def solution(s):
    s_list = sorted([x for x in s if s.count(x) == 1])
    answer = ''.join(s_list)
    return answer