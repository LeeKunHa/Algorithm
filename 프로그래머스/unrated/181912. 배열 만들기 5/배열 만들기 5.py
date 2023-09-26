def solution(intStrs, k, s, l):
    answer = list(map(int,[x[s:s+l] for x in intStrs if int(x[s:s+l])> k]))
    return answer