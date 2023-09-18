def solution(array, commands):
    answer = [sorted(array[x[0]-1:x[1]])[x[2]-1] for x in commands]
    return answer