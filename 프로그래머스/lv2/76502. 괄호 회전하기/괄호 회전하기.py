from collections import deque
def solution(s):
    dic = {']':'[','}':'{',')':'('}
    s = deque(s)
    answer = 0
    for i in range(len(s)):
        succes = True
        stack = []
        for j in range(len(s)):
            if s[j] in ['[','{','(']:
                stack.append(s[j])
            elif stack and stack[-1]==dic[s[j]]:
                stack.pop()
                pass
            else:
                succes = False
        if succes and not stack:
            answer = answer+1
        s.rotate(-1)
    return answer