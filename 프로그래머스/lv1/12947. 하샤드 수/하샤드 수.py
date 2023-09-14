def solution(x):
    sum_ = sum([int(x) for x in str(x)])
    if x%sum_ == 0:
        answer = True
    else:
        answer = False
    return answer