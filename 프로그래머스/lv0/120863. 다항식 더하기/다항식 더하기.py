def solution(polynomial):
    polynomial = polynomial.split(' + ')
    a,b = 0,0
    for i in polynomial:
        if i == 'x':
            i = '1x'
        if i[-1] == 'x':
            a = a+int(i[:-1])
        else:
            b = b+int(i)
    if a == 1:
        a = ''
    if a == 0:
        answer = str(b)
    elif b == 0:
        answer = str(a)+'x'
    else:
        a = str(a)+'x'
        b = str(b)
        answer = ' + '.join([a,b])
    return answer