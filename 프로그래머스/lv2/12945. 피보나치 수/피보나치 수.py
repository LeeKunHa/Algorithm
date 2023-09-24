"""
def solution(n):
    if n < 2:
        return n
    else:
        return (solution(n-1)+solution(n-2)) % 1234567
"""

def solution(n):
    a,b = 0,1
    for i in range(n):
        a,b = b,a+b
    answer = a
    return answer % 1234567