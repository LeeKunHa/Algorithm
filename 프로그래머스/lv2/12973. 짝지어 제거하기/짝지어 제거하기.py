def solution(s):
    s = list(s)
    stack = [s[0]]
    for i in range(1,len(s)):
        if stack and s[i]==stack[-1]:
            stack.pop()
        else:
            stack.append(s[i])
    if stack:
        answer = 0
    else:
        answer = 1
    return answer