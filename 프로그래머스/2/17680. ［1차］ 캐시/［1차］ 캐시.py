def solution(cacheSize, cities):
    answer = 0
    stack = []
    for i in cities:
        i = i.lower()
        if i not in stack:
            answer = answer+5
            stack.append(i)
        else:
            answer = answer+1
            stack.remove(i)
            stack.append(i)
        if len(stack)>cacheSize:
            stack.pop(0)
    return answer