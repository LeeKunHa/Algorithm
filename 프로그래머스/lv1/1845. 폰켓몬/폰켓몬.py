def solution(nums):
    n = int(len(nums)/2)
    unique = list(set(nums))
    answer = min(n,len(unique))
    return answer