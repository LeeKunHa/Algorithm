def solution(num_list):
    odd = ''.join([str(x) for x in num_list if x%2==1])
    even = ''.join([str(x) for x in num_list if x%2==0])
    answer = int(odd)+int(even)
    return answer