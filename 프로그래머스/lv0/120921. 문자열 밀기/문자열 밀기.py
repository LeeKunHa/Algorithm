def solution(A, B):
    A = list(A)
    if ''.join(A)==B:
        return 0
    for i in range(1,len(A)+1):
        string = A.pop()
        A.insert(0,string)
        if ''.join(A)==B:
            return i
    return -1