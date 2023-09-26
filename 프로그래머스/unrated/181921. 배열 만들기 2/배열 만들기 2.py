def solution(l, r):
    answer = [str(x).replace('5','a').replace('0','b') for x in list(range(l,r+1))]
    answer = [x for x in answer if x.isalpha()]
    answer = list(map(int,[x.replace('a','5').replace('b','0') for x in answer]))
    if answer == []:
        answer = [-1]
    return answer