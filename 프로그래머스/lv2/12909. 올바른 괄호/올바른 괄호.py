def solution(s):
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if stack:
                stack.pop()
            else:
                return False
    # 리스트에 '('가 남아 있어도 실패
    if stack:
        return False
    return True