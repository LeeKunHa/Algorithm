from itertools import combinations
def solution(number):
    answer = len([x for x in list(combinations(number,3)) if sum(x)==0])
    return answer