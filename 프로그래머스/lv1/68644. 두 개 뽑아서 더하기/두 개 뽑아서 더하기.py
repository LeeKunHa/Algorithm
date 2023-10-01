from itertools import combinations
def solution(numbers):
    answer = sorted(list(set([sum(x) for x in list(combinations(numbers,2))])))
    return answer