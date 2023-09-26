def solution(a, b):
    a,b = str(a),str(b)
    answer = a+b
    if int(a+b) < int(b+a):
        answer = b+a
    return int(answer)