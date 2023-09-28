import math
def solution(a, b):
    gcd = math.gcd(a,b)
    b = b//gcd
    i = 2
    num_list = []
    while b>=i:
        if b%i==0:
            b = b//i
            num_list.append(i)
        else:
            i = i+1
    if [x for x in num_list if x not in [2,5]]==[]:
        answer=1
    else:
        answer=2
    return answer