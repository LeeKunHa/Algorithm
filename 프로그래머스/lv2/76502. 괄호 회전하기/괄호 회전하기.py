from collections import deque
def solution(s):
    answer = 0
    dic = dict({')':'(', ']':'[', '}':'{'})
    stack = []
    queue = deque(s)
    for i in range(len(s)):
        try:
            for j in queue:
                if j in ('(','[','{'):
                    stack.append(j)
                elif stack[-1] == dic[j]:
                    stack.pop()
            if stack == []:
                answer = answer+1
        except:
            pass
        queue.rotate(-1)
    return answer