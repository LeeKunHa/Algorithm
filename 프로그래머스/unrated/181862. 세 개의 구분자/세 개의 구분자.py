def solution(myStr):
    answer = list(filter(None,myStr.replace('a',' ').replace('b',' ').replace('c',' ').split(' ')))
    if answer == []:
        answer.append('EMPTY')
    return answer