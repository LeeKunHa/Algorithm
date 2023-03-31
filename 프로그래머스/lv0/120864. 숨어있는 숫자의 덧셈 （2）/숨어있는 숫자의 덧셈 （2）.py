def solution(my_string):
    answer = 0
    num_string = ''
    for i in my_string:
        if i.isdigit():
            num_string = num_string+str(i)
        else:
            num_string = num_string+' '
    num_string = num_string.split(' ')
    for j in num_string:
        if j.isdigit():
            answer = answer+int(j)
    return answer