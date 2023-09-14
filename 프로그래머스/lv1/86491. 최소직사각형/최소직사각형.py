import numpy as np
def solution(sizes):
    for i in sizes:
        if i[0] > i[1]:
            i[0],i[1] = i[1],i[0]
    answer = int(np.max(sizes, axis=0)[0]) * int(np.max(sizes, axis=0)[1])
    return answer