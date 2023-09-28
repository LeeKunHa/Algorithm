from itertools import combinations
def solution(dots):
    gradient = []
    line_pair = list(combinations(dots,2))
    d1 = abs(line_pair[0][0][1]-line_pair[0][1][1])/abs(line_pair[0][0][0]-line_pair[0][1][0])
    d2 = abs(line_pair[-1][0][1]-line_pair[-1][1][1])/abs(line_pair[-1][0][0]-line_pair[-1][1][0])
    if d1==d2:
        answer=1
    else:
        answer=0
    return answer