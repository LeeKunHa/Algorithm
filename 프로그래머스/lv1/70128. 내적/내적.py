#import numpy as np
#def solution(a, b):
#    answer = int(np.dot(a,b))
#    return answer

def solution(a, b):
    answer = 0
    for i in range(len(a)):
        single = a[i]*b[i]
        answer = answer+single
    return answer