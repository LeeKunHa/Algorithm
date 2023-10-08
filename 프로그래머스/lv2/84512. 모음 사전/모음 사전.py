from itertools import product
def solution(word):
    dic = ['A','E','I','O','U']
    answer = []
    for i in range(1,len(dic)+1):
        answer.append([''.join(x) for x in list(product(dic,repeat=i))])
    answer = sorted(sum(answer,[]))
    answer = answer.index(word)+1
    return answer