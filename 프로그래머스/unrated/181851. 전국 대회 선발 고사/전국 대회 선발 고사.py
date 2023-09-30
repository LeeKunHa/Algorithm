def solution(rank, attendance):
    student = [[i,x] for i,x in enumerate(rank) if attendance[i]]
    student = [x[0] for x in sorted(student, key=lambda x:x[1])][:3]
    answer = 0
    for i,j in zip(student,[10000,100,1]):
        answer = answer+i*j
    return answer