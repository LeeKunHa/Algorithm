def solution(dots):
    x_list = []
    y_list = []
    dots = sum(list(dots),[])
    for i in range(len(dots)):
        if i%2 == 0:
            x_list.append(dots[i])
        elif i%2 == 1:
            y_list.append(dots[i])
    answer = abs(max(x_list)-min(x_list)) * abs(max(y_list)-min(y_list))
    return answer