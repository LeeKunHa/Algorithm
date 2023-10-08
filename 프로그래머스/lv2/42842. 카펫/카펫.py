def solution(brown, yellow):
    target = brown+yellow
    for i in range(1,target+1):
        if target%i == 0:
            x = target//i
            y = i
            if (2*x)+(2*y)==brown+4:
                answer = sorted([x,y],reverse=True)
    return answer