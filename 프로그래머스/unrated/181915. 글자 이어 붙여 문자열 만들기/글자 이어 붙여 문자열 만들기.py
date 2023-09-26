def solution(my_string, index_list):
    dic = dict([x for x in enumerate(my_string)])
    answer = ''.join([dic[x] for x in index_list])
    return answer