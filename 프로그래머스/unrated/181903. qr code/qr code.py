def solution(q, r, code):
    answer = ''.join([code[x] for x in range(len(code)) if x%q==r])
    return answer