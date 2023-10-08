from itertools import permutations
def solution(numbers):
    answer = []
    for n in range(1,len(numbers)+1):
        target = list(set([int(''.join(x)) for x in list(permutations(numbers,n))]))
        temp = []
        for i in target:
            if i not in [0,1] and is_prime(i):
                temp.append(i)
        answer.append(temp)
    answer = len(set(sum(answer,[])))
    return answer

def is_prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True