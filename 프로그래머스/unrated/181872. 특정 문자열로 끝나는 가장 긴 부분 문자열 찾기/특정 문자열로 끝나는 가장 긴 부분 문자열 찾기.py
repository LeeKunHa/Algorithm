def solution(myString, pat):
    answer = myString
    string = ''
    for i in myString:
        string=string+i
        if string[-len(pat):]==pat:
            answer=string
    return answer