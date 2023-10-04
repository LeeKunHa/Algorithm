def solution(elements):
    elements = elements*2
    sum_list = []
    for i in range(len(elements)//2):
        for j in range(len(elements)//2):
            sum_list.append(sum(elements[j:j+i+1]))
    answer = len(set(sum_list))
    return answer