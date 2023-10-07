def solution(numbers):
    if set([x for x in numbers]) == set([0]):
        return '0'
    answer = ''.join(sorted(list(map(str, numbers)), key=lambda x:x*3, reverse=True))
    return answer