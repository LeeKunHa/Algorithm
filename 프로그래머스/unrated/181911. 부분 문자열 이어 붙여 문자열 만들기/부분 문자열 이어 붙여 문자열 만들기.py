def solution(my_strings, parts):
    answer = ''.join([x[i[0]:i[1]+1] for x,i in zip(my_strings,parts)])
    return answer