def solution(str_list):
    l_index = ''.join(str_list).find('l')
    r_index = ''.join(str_list).find('r')
    if l_index == r_index == -1:
        answer = []
    elif l_index == -1:
        answer = str_list[r_index+1:]
    elif r_index == -1:
        answer = str_list[:l_index]
        
    elif l_index<r_index:
        answer = str_list[:l_index]
    else:
        answer = str_list[r_index+1:]
    return answer