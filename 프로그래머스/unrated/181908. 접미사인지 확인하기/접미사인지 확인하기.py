def solution(my_string, is_suffix):
    answer = int(my_string[-len(is_suffix):] == is_suffix)
    return answer