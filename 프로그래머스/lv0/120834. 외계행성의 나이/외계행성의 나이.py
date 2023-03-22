def solution(age):
    answer = ''
    alpha = ['a','b','c','d','e','f','g','h','i','j']
    for i in str(age):
        answer = answer+(alpha[int(i)])
    return str(answer)