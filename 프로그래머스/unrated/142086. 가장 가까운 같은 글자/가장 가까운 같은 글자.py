def solution(s):
    answer = []
    stack = []
    for i,x in enumerate(s):
        if x not in stack:
            answer.append(-1)
        else:
            answer.append(abs(''.join(stack).rfind(x)-i))
        stack.append(x)
    return answer