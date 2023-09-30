def solution(arr):
    stk = []
    i = 0
    while i<=(len(arr)-1):
        if not stk:
            stk.append(arr[i])
            i = i+1
            continue
        elif stk and stk[-1]<arr[i]:
            stk.append(arr[i])
            i = i+1
            continue
        elif stk and stk[-1]>=arr[i]:
            stk.pop()
    return stk