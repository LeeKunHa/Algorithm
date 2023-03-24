def solution(n):
    num = 1
    fac = 1
    while n>=fac:
        fac = fac*num
        num = num+1
    return num-2