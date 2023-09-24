def solution(s):
    num_list = s.split()
    num_list = [int(x) for x in num_list]
    answer = f"{min(num_list)} {max(num_list)}"
    return answer