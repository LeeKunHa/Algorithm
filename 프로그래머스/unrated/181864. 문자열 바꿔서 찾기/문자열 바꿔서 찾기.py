def solution(myString, pat):
    new_string=''
    dic = {'A':'B', 'B':'A'}
    for i in myString:
        new_string=new_string+(dic[i])
    answer = int(pat in new_string)
    return answer