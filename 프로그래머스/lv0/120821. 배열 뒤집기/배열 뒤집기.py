def solution(num_list):
    answer = []
    num_list_ = num_list.copy()
    for i in num_list:
        answer.append(num_list_.pop())
    return answer