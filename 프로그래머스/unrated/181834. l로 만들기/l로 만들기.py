def solution(myString):
    answer=''
    for i in myString:
        if i in ['a','b','c','d','e','f','g','h','i','j','k']:
            answer=answer+'l'
        else:
            answer=answer+i
    return answer