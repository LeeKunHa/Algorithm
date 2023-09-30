def solution(ineq, eq, n, m):
    if eq == '!': eq=''
    answer = eval(''.join(list(map(str,[n,ineq,eq,m]))))
    return int(answer)