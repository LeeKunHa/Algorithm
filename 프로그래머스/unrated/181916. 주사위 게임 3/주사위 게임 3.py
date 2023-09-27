from collections import Counter

def solution(a, b, c, d):
    if len(set([a,b,c,d]))==1:
        answer = a*1111
    elif len(set([a,b,c,d]))==2 and (Counter([a,b,c,d]).most_common(1)[0][1] == 3):
        answer = (10*Counter([a,b,c,d]).most_common(2)[0][0]+Counter([a,b,c,d]).most_common(2)[1][0])**2
    elif len(set([a,b,c,d]))==2 and (Counter([a,b,c,d]).most_common(1)[0][1] == 2):
        answer = (Counter([a,b,c,d]).most_common(2)[0][0] + Counter([a,b,c,d]).most_common(2)[1][0]) * abs(Counter([a,b,c,d]).most_common(2)[1][0] - Counter([a,b,c,d]).most_common(2)[0][0])
    elif len(set([a,b,c,d]))==3:
        answer = Counter([a,b,c,d]).most_common(3)[1][0]*Counter([a,b,c,d]).most_common(3)[2][0]
    else:
        answer = min(a,b,c,d)
    return answer