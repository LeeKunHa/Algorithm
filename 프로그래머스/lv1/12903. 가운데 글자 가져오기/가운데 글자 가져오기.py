def solution(s):
    if len(s)%2 == 0:
        mid_idx = int(len(s)/2 - 0.5)
        answer = s[mid_idx:mid_idx+2]
    else:
        mid_idx = int(len(s)/2)
        answer = s[mid_idx]
    return answer